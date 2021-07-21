from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CustomUserCreationForm

class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
"""
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url= reverse_lazy('home')
    template_name = 'registration/password_reset_form.html'
"""