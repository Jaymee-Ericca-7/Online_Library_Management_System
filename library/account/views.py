from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, AccountAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


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

@login_required
def profile(request):
    return render(request, 'account/profile.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'account/change_password.html', {
        'form': form
    })

def login_view(request):
    user = request.user
    if user.is_authenticated:
        print("user already authenticated")
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



# Create your views here.
