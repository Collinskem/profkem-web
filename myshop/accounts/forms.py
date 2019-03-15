from django.contrib.auth.forms import AuthenticationForm
from django import forms
class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )
    phone=forms.IntegerField(
    required=True,
    label='phone',

    )


class LoginForm(forms.Form):
        email =forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
        password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
