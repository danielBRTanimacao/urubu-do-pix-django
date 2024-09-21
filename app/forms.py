from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegisterForm(UserCreationForm):

    username = forms.CharField(
        label='Nome de usuario',
        widget=forms.TextInput(),
        required=True,
        min_length=3,
    )
    password1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'id': 'passwordInput',
            }
        ),
        required=True,
        min_length=3
    )
    password2 = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(),
        required=True,
        min_length=3
    )

    class Meta:
        model = User
        fields = (
            'username', 'password1', 'password2',
        )
    

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Seu nome',
        widget=forms.TextInput(),
        required=True,
        min_length=3,
    )
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={
                'id': 'passwordInput'
            }
        ),
        required=True,
        min_length=3,
    )

    class Meta:
        model = User
        fields = (
            'username', 'password'
        )