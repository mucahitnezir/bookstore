from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from crispy_forms.helper import FormHelper

from user.models import User


class LoginForm(AuthenticationForm):
    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False
        return helper


class RegisterForm(forms.ModelForm):
    email = forms.EmailField(label=_('email address'))
    password = forms.CharField(label='Şifre', widget=forms.PasswordInput())

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False
        return helper

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'phone', 'password'
