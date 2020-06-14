from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from .models import *
from django.contrib.auth.models import *
import time
import datetime
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

def redirect_to_test(request):
    return redirect('test/', permanent=True)

class Test(LoginRequiredMixin, View):
    def get(self, request):
        name = Client.objects.all()
        return HttpResponse(name)
