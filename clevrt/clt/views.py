from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, reverse, get_object_or_404
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
from django.db import transaction
import re
from django.http import JsonResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
import random
from django.core.exceptions import MultipleObjectsReturned

class Index(View):
    template_name = 'clt/index.html'
    def get(self, request):
        print(request.user.id)
        if Client.objects.filter().count() > 10:
            last_active = Client.objects.filter().order_by('-last_activity')[:9]
        elif Client.objects.filter().count() > 0:
            last_active = Client.objects.filter().order_by('-last_activity')[:Client.objects.filter().count()]
        else:
            last_active = {}

        if Reminder.objects.filter().count() > 8:
            reminders = Reminder.objects.filter()[:7]
        elif Reminder.objects.filter().count() > 0:
            reminders = Reminder.objects.filter()[:Reminder.objects.filter().count()]
        else:
            reminders = {}
        return render(request, template_name=self.template_name, context={'last_active': last_active, 'reminders': reminders})

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
            if client_numbers.is_valid() and ip_list.is_valid() and client_gateways.is_valid():
                self.object = form.save()
                ip_list.instance = self.object
                ip_list.save()
                client_gateways.instance = self.object
                client_gateways.save()
                client_numbers.instance = self.object
                client_numbers.save()
            else:
                return super().form_invalid(form)

        return super(ClientCreate, self).form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


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
        else:
            data['client'] = self.model.objects.get(pk=self.object.pk)
            data['title'] = "Изменить клиента"
            data['ip_list'] = Ip_ListFormSet(instance=self.object)
            data['client_numbers'] = Client_NumberFormSet(instance=self.object)
            data['client_gateways'] = Client_GatewayFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ip_list = context['ip_list']
        client_numbers = context['client_numbers']
        client_gateways = context['client_gateways']
        with transaction.atomic():
            if ip_list.is_valid() and client_numbers.is_valid() and client_gateways.is_valid():
                self.object = form.save()
                ip_list.instance = self.object
                ip_list.save()
                client_numbers.instance = self.object
                client_numbers.save()
                client_gateways.instance = self.object
                client_gateways.save()
            else:
                return super().form_invalid(form)

        return super(ClientUpdate, self).form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()


class Clients(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clt/client_list.html'

    def post(self, request):
        data = ''
        if ('country' in self.request.POST and 'city' in self.request.POST):
            data = CityForm(self.request.POST)
            if data.is_valid():
                data.save()
                data = 'Done'
            else:
                data = data.errors['city']
        elif 'country' in self.request.POST:
            data = CountryForm(self.request.POST)
            if data.is_valid():
                data.save()
                data = 'Done'
            else:
                data = data.errors['country']
        elif 'number' in self.request.POST:
            data = Client_NumberForm(self.request.POST)
            if data.is_valid():
                data.save()
                data = 'Done'
            else:
                data = data.errors['number']
        elif 'text' in self.request.POST:
            data = ReminderForm(self.request.POST)
            if data.is_valid():
                instance = data.save(commit=False)
                instance.created_user = request.user
                instance.save()
                data = 'Done'
            else:
                data = data.errors['text']
        return HttpResponse(data)

    def get_context_data(self, **kwargs):
        data = super(Clients, self).get_context_data(**kwargs)
        if self.request.method == 'GET':
            data['active_clients'] =  self.model.objects.filter(client_status='On', hide=False).order_by('name')
            data['potential_clients'] = self.model.objects.filter(client_status='Pot', hide=False).order_by('name')
            data['disabled_clients'] = self.model.objects.filter(client_status='Off', hide=False).order_by('name')
            data['cities'] = City.objects.all().order_by('city')
            data['countries'] = Country.objects.all().order_by('country')
            data['country_form'] = CountryForm()
            data['city_form'] = CityForm()
            data['number_form'] = Client_NumberForm()
            return data


class ClientView(LoginRequiredMixin, View):
    model = Client
    template_name = 'clt/client.html'

    def get(self, request, pk):
        client_info = get_object_or_404(self.model, pk=pk)
        gateways = Client_Gateway.objects.filter(client=client_info.pk)
        numbers = Client_Number.objects.filter(client=client_info.pk, hide=False)
        ip_list = Ip_List.objects.filter(client=client_info.pk)
        self.model.objects.filter(pk=pk).update(last_activity=datetime.now())

        return render(request, self.template_name, {'client': client_info, 'gateways': gateways, 'numbers': numbers, 'ip_list': ip_list})

class Clt_Info(View):
    def post(self, request):
        action = request.POST['action']
        if action == 'ssh-connect':
            client_id = request.POST['client']
            ip_list = Ip_List.objects.filter(client=client_id)
            gataways = Client_Gateway.objects.filter(client=client_id)
            data_ip = {}
            for i, ip in enumerate(ip_list):
                data_ip[i] = ip.ip + ":" + ip.port
            gateways_tunnels = {}
            localhost_port = random.randint(14332, 24200)
            for gateway in gataways:
                tunnel_port = random.randint(24400, 65634)
                gateways_tunnels[tunnel_port] = gateway.ip + ":" + gateway.port

            return JsonResponse({'ip_list': data_ip, 'gateways': gateways_tunnels, 'localhost_port': localhost_port})
        elif action == 'reminder-view':
            reminder_id = request.POST['reminderId']
            reminder = Reminder.objects.get(pk=reminder_id)
            reminder.users.add(request.user.id)

            return HttpResponse('Reminder Done')


class Clt_SSHInfo(View):
    def get(self,request):
        prefix = 'http://localhost:'
        localhost_port = self.request.GET['localhost_port']
        localhost_link = prefix + localhost_port
        localhost_link_root = prefix + localhost_port + '/root'
        client = self.request.GET['client']
        title = Client.objects.get(id=client).name
        ip = self.request.GET['ip']
        request_length = len(self.request.GET) - 3
        gateways = []
        print(int((request_length / 2))+1)
        for i in range(1, int((request_length / 2))+1):
            print(i)
            gateway_ip = self.request.GET['gateway{}_ip'.format(i)]
            tunnel_port = self.request.GET['gateway{}_port'.format(i)]
            try:
                gateway = Client_Gateway.objects.get(client=client, ip=gateway_ip.split(':')[0], port=gateway_ip.split(':')[1])
                gateway_password = gateway.secret
                gateway_login = gateway.login
                gateway_type = gateway.type_gateway
                # print(f'Link: {prefix}{tunnel_port} | Gateway IP: {gateway_ip} | Login: {gateway_login} | Secret: {gateway_password} | Gateway Type: {gateway_type}')
                gateways.append({'link': prefix + tunnel_port, 'ip': gateway_ip, 'login': gateway_login, 'secret': gateway_password, 'type': gateway_type})
            except MultipleObjectsReturned:
                pass
        return render(request, template_name='clt/ssh-info.html', context={'ip': ip, 'localhost_link': localhost_link, 'localhost_link_root': localhost_link_root, 'title': title, 'gateways': gateways})