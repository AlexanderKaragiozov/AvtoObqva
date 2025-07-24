# forms.py
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django import  forms
from django.contrib.auth.models import User

from user.models import Profile


class StyledLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Потребителско име'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Парола'
        })
    )

class StyledRegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Потребителско име'
        })
    )
    password1 = forms.CharField(
        label="Парола",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Парола'
        })
    )
    password2 = forms.CharField(
        label="Повтори парола",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Повтори парола'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

    first_name = forms.CharField(
        label="Име",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Иван'
        })
    )
    last_name = forms.CharField(
        label="Фамилно име",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Иванов'
        })
    )
    phone_number = forms.CharField(
        label="Тел. Номер",
        widget=forms.TextInput(attrs={

            'placeholder': '0897327xxxx'
        })
    )
    location = forms.CharField(
        label="Местоживеене",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Пример: София'
        })
    )
    profile_image = forms.ImageField(
        label="Аватар",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
        })
    )