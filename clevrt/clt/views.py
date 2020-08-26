from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, reverse, render
from .models import *
from django.contrib.auth.models import *
import time
import datetime
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.forms import ValidationError
import re

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
    success_url = reverse_lazy('clt:test')
    print(0)
    # def form_invalid(self, form):
    #     print(444444444444444444)
    #     name = self.request.POST['name']
    #     print(name)
    #     if len(self.model.objects.filter(name=name)) > 0:
    #       print('pizda')
    #       #form.errors['name'][0] = 'PIZDA'
    #       raise ValidationError('PIZDEC')
    #
    #     return super().form_invalid(form)


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        print(1)
        if self.request.POST:
            name = self.request.POST['name']
            print(name)
            print(self.model.objects.filter(name=name))
            print(len(self.model.objects.filter(name=name)))
            print(2)
            data['children'] = ChildFormSet(self.request.POST)
            data['c'] = CFormSet(self.request.POST)
            print(3)
            print(data)
        else:
            print(999)
            data['children'] = ChildFormSet()
            data['c'] = CFormSet()
        print(4)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        familymembers = context['children']
        c = context['c']
        print(5)
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
                    'officeIp2', 'officeIp3', 'officeIp4', 'client_status', 'os_version',
              'ast_version', 'login_ccs', 'secret_ccs', 'ccs_version', 'cphone_maxvers',
                    'vps_own', 'hide', 'additional_info', 'date_on', 'date_off', ]
    success_url = reverse_lazy('clt:clients')

    def form_invalid(self, form):
        name = self.request.POST['name']
        if len(self.model.objects.filter(name=name)) > 0:
            form.errors['name'][0] = 'Клиент с таким названием уже существует'
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        data = super(ClientCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['ip_list'] = Ip_ListFormSet(self.request.POST)
            data['client_numbers'] = Client_NumberFormSet(self.request.POST)
            data['client_gateways'] = Client_GatewayFormSet(self.request.POST)
        else:
            data['ip_list'] = Ip_ListFormSet()
            data['client_numbers'] = Client_NumberFormSet()
            data['client_gateways'] = Client_GatewayFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ip_list = context['ip_list']
        client_numbers = context['client_numbers']
        client_gateways = context['client_gateways']
        if client_numbers.is_valid() and ip_list.is_valid() and client_gateways.is_valid():
            ip_list.instance = form.save()
            ip_list.save()
            client_gateways.instance = form.save()
            client_gateways.save()
            client_numbers.instance = form.save()
            client_numbers.save()
        else:
            if len(client_numbers.errors[0]) > 0:
                number = str(self.request.POST['client_number_set-0-number'])
                name = str(self.request.POST['client_number_set-0-name'])
                print(name)
                if name == '' or None:
                    client_numbers.errors[0]['name'][0] = "Необходимо заполнить имя"
                check_number = Client_Number.objects.filter(number=number)
                client_numbers.errors[0]['number'][0] = "Номер {} уже закреплен за клиентом {}".format(number, str(check_number[0]))

                return render(self.request, 'clt/client_form.html',
                              {'form': form, 'client_numbers': client_numbers, 'client_gateways': client_gateways,
                                                           'ip_list': ip_list, 'formset_errors': client_numbers.errors})
        return super(ClientCreate, self).form_valid(form)


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

