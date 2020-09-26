from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from library_system.models import Book
from library_system.models import BookInstance
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    books = Book.objects.all()
    args = {'books': books}
    return render(request, 'users/profile.html', args)

@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    request.session['isLoggedIn'] = True
    request.session['isAdmin'] = user.is_superuser
    isLoggedIn = request.session.get('isLoggedIn',False)
    isAdmin = request.session.get('isAdmin',False)
    request.session.set_expiry(10)
  #  return render(
   #     request,
   #     'users/login.html',
    #    context = {'isLoggedIn':isLoggedIn,'isAdmin':isAdmin},
    #)
