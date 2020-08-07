from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, reverse, render
from .models import *
from django.contrib.auth.models import *
import time
import datetime
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.db import transaction
from django.core.exceptions import ValidationError

class Index(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, template_name=self.template_name)

class Test(ListView):
    model = Test_Model
    #data = model.objects.all()
    #template_name = 'test_model_list.html'

    #def get(self, request, *args, **kwargs):
    #    render(request, template_name=self.template_name)

class TestDetail(CreateView):
    model = Test_Model
    fields =['name',]
    error_messages = {'name': {'unique_together': 'Такой клиент уже существует'}}
    success_url = reverse_lazy('clt:test')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['children'] = ChildFormSet(self.request.POST)
            data['c'] = CFormSet(self.request.POST)
        else:
            data['children'] = ChildFormSet()
            data['c'] = CFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['children']
        c = context['c']
        if self.model.objects.get(name=form.name):
            raise ValidationError(_('Такой клиент уде существует'))
        self.object = form.save()
        if familymembers.is_valid():
            familymembers.instance = self.object
            familymembers.save()
        if c.is_valid():    
            c.instance = self.object
            c.save()
        return super(TestDetail, self).form_valid(form)


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    fields = ['name', 'country', 'city', 'hostname', 'gateway_info', 'local_ip', 'title_comment', 'officeIp1',
                    'officeIp2', 'officeIp3', 'officeIp4', 'client_status', 'os_version', 'ast_version',
                    'vps_own', 'hide', 'additional_info', 'date_on', 'date_off', ]
    success_url = reverse_lazy('clt:test')

    def get_context_data(self, **kwargs):
        data = super(ClientCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            print(self.request.POST)
            data['ip_list'] = Ip_ListFormSet(self.request.POST)
            data['client_numbers'] = Client_NumberFormSet(self.request.POST)
            data['client_gateways'] = Client_GatewayFormSet(self.request.POST)
            data['ccs'] = CCSFormSet(self.request.POST)
        else:
            data['ip_list'] = Ip_ListFormSet()
            data['client_numbers'] = Client_NumberFormSet()
            data['client_gateways'] = Client_GatewayFormSet()
            data['ccs'] = CCSFormSet()
        return data


class Clients(LoginRequiredMixin, ListView):
    model = Client

    def get_context_data(self, **kwargs):
        data = {'active_clients': self.model.objects.filter(client_status='On').order_by('name'),
                'potential_clients': self.model.objects.filter(client_status='Pot').order_by('name'),
                'disabled_clients': self.model.objects.filter(client_status='Off').order_by('name'),
                'cities': City.objects.all().order_by('city'),
                'countries': Country.objects.all().order_by('country')}
        if self.request.method == 'GET':
            return data




class ClientView(LoginRequiredMixin, DetailView):
    model = Client

