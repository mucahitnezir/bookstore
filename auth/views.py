from django.contrib import messages
from django.contrib.auth import views as auth_views, authenticate, login
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.views.generic import CreateView

from auth.forms import LoginForm, RegisterForm
from user.models import User


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    extra_context = {'title': _('Login')}


class LogoutView(auth_views.LogoutView):
    pass


class RegisterView(SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('landing:home')
    success_message = _('Your membership created successfully.')
    extra_context = {'title': _('Register')}

    def form_valid(self, form):
        # Create user row
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        # Login
        new_user = authenticate(username=user.username, password=password)
        login(self.request, new_user)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.warning(self.request, _('Form is invalid. Please try again.'))
        return super().form_invalid(form)
