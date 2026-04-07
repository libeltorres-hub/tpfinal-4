from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'link', 'birthday']
        labels = {
            'bio': 'Biografía',
            'link': 'Sitio web',
            'birthday': 'Fecha de nacimiento',
        }
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
