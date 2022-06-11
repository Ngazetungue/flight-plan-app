from django.http.response import HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth import get_user_model

from users.forms import CustomUserCreationForm

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

    def form_valid(self, form):
        form.save()  # save the user
        return super().form_valid(form)

def check_username(request):
    username = request.POST.get('username')
    if get_user_model().objects.filter(username=username).exists():
        return HttpResponse("This username already exists")
    else:
        return HttpResponse("")

"""
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url= reverse_lazy('home')
    template_name = 'registration/password_reset_form.html'
"""