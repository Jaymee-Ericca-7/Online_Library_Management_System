from django import forms
from collections import OrderedDict
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth.forms import authenticate

from account.models import Account

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Account
        fields = ("email", "username", 'first_name', 'last_name', "id_num", "password1", "password2")

class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('username', 'password')
    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username = username, password = password):
                raise forms.ValidationError("Invalid Login / Too many attempts")




