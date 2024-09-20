from .models import User
from django import forms

class UserForm(forms.ModelForm):

    username = forms.CharField(
        label='Nome de usuario',
        widget=forms.TextInput(
            attrs={
                'class': 'input'
            }
        ),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']