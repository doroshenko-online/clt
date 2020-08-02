from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, reverse, render
from .models import *
from django.contrib.auth.models import *
import time
import datetime
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *

class Index(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, template_name=self.template_name)

class Test(View):
    model = Test_Model
    template_name = 'test.html'
    form_class = TestForm
    success_url = '/'
    def get(self, request, *args, **kwargs):
        form = TestFormSet
        print(form)
        return render(request, template_name=self.template_name, context={'form': form})

    #def post(self, request, *args, **kwargs):
   #     form = TestFormSet
   #     d
        

class Clients(View):
    template_name = 'clients.html'
    def get(self, request):
        return render(request, template_name=self.template_name)

class ClientView(View):
    template_name = 'client.html'
    def get(self, request):
        return render(request, template_name=self.template_name)

class Add_Client(View):
    template_name = 'add-change-client.html'
    def get(self, request):
        return render(request, template_name=self.template_name)
