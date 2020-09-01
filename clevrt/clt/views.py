from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, reverse, render, get_object_or_404
from .models import *
from django.contrib.auth.models import *
import time
from datetime import datetime
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.forms import ValidationError
from django.db import transaction
import re

class Index(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request, template_name=self.template_name)


class ClientCreate(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm

    def get_context_data(self, **kwargs):
        data = super(ClientCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['title'] = "Добавить клиента"
            data['ip_list'] = Ip_ListFormSet(self.request.POST)
            data['client_numbers'] = Client_NumberFormSet(self.request.POST)
            data['client_gateways'] = Client_GatewayFormSet(self.request.POST)
        else:
            data['title'] = "Добавить клиента"
            data['ip_list'] = Ip_ListFormSet()
            data['client_numbers'] = Client_NumberFormSet()
            data['client_gateways'] = Client_GatewayFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ip_list = context['ip_list']
        client_numbers = context['client_numbers']
        client_gateways = context['client_gateways']
        with transaction.atomic():
            self.object = form.save()
            if client_numbers.is_valid() and ip_list.is_valid() and client_gateways.is_valid():
                ip_list.instance = self.object
                ip_list.save()
                client_gateways.instance = self.object
                client_gateways.save()
                client_numbers.instance = self.object
                client_numbers.save()

        return super(ClientCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('clt:client', kwargs={'pk': self.object.pk})


class ClientUpdate(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm

    def get_context_data(self, **kwargs):
        data = super(ClientUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['title'] = "Изменить клиента"
            data['ip_list'] = Ip_ListFormSet(self.request.POST, instance=self.object)
            data['client_numbers'] = Client_NumberFormSet(self.request.POST, instance=self.object)
            data['client_gateways'] = Client_GatewayFormSet(self.request.POST, instance=self.object)
            print(data['client_numbers'])
        else:
            data['title'] = "Изменить клиента"
            data['ip_list'] = Ip_ListFormSet(instance=self.object)
            data['client_numbers'] = Client_NumberFormSet(instance=self.object)
            data['client_gateways'] = Client_GatewayFormSet(instance=self.object)
            print(data['client_numbers'])
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ip_list = context['ip_list']
        client_numbers = context['client_numbers']
        client_gateways = context['client_gateways']
        print(client_numbers.errors)
        print(ip_list.errors)
        print(client_gateways.errors)
        with transaction.atomic():
            self.object = form.save()
            if ip_list.is_valid() and client_numbers.is_valid() and client_gateways.is_valid():
                ip_list.instance = self.object
                ip_list.save()
                client_numbers.instance = self.object
                client_numbers.save()
                client_gateways.instance = self.object
                client_gateways.save()

        return super(ClientUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('clt:client', kwargs={'pk': self.object.pk})


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




class ClientView(LoginRequiredMixin, View):
    model = Client
    template_name = 'client.html'

    def get(self, request, pk):
        client_info = get_object_or_404(self.model, pk=pk)
        gateways = Client_Gateway.objects.filter(client=client_info.pk)
        numbers = Client_Number.objects.filter(client=client_info.pk)
        ip_list = Ip_List.objects.filter(client=client_info.pk)
        self.model.objects.filter(pk=pk).update(last_activity=datetime.now())

        return render(request, self.template_name, {'client': client_info, 'gateways': gateways, 'numbers': numbers, 'ip_list': ip_list})

