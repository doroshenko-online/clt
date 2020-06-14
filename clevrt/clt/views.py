from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth.models import *
import time
import datetime
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import FormView
from django.views.generic.base import View

# Create your views here.
class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')