from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('libsys-home')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            print("form is valid. user authenticated")
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                print(user)
                login(request, user)
                return render(request, 'library_system/home.html')

    else:
        form = AccountAuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'account/logout.html')

@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    request.session['isLoggedIn'] = True
    request.session['isAdmin'] = user.is_superuser
    request.session['role'] = user.role
    request.session['username'] = user.username
    isLoggedIn = request.session.get('isLoggedIn',False)
    isAdmin = request.session.get('isAdmin',False)
    print(request.session['isLoggedIn'])
    print(request.session['username'])
    print(request.session['role'])
    request.session.set_expiry(60)
