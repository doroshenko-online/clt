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

class Index(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, template_name=self.template_name)

class Test(LoginRequiredMixin, View):
    def get(self, request):
        name = Client.objects.all()
        return HttpResponse(name)

class Clients(View):
    template_name = 'clients.html'
    def get(self, request):
        return render(request, template_name=self.template_name)
