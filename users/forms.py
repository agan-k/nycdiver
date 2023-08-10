from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

username_validator = UnicodeUsernameValidator()

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label=_('Username* '), 
        max_length=150, 
        validators=[username_validator],
        error_messages={'unique': _("A user with that username already exists.")},
        widget=forms.TextInput(attrs={'class': 'form-label form-label--username'})
    )
    password1 = forms.CharField(
        label=_('Password** '),
        widget=(forms.PasswordInput(attrs={'class': 'form-label form-label--password1'})),
    )
    password2 = forms.CharField(
        label=_('Password Confirmation'), 
        widget=forms.PasswordInput(attrs={}),
        help_text=_('Just Enter the same password, for confirmation')
    )