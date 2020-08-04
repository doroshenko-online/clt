from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect, reverse, render
from .models import *
from django.contrib.auth.models import *
import time
import datetime
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.urls import reverse_lazy
from django.db import transaction

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
    fields =['name', 'title', 'comment']
    success_url = reverse_lazy('clt:test')

    def get_context_data(self, **kwargs):
        data = super(TestDetail, self).get_context_data(**kwargs)
        if self.request.POST:
            data['children'] = ChildFormSet(self.request.POST)
        else:
            data['children'] = ChildFormSet()
        return data

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     familymembers = context['children']
    #     with transaction.atomic():
    #         self.object = form.save()
    #
    #         if familymembers.is_valid():
    #             familymembers.instance = self.object
    #             familymembers.save()
    #     return super(TestDetail, self).form_valid(form)
    # def get(self, request, *args, **kwargs):
    #     data = self.model_data.objects.get(id=kwargs['test_id'])
    #     #ChildFormSet = inlineformset_factory(Test_Model, Test_Child, fields=('info',), extra=1)
    #     formset = ChildFormSet(instance=data)
    #     return render(request, template_name=self.template_name, context={'data': data, 'formset': formset})
    #
    # def post(self, request, *args, **kwargs):
    #     #ChildFormSet = inlineformset_factory(Test_Model, Test_Child, fields=('info',), extra=1)
    #     data = self.model_data.objects.get(id=kwargs['test_id'])
    #     formset = ChildFormSet(request.POST, instance=data)
    #     if formset.is_valid():
    #         formset.save()
    #     formset = ChildFormSet(instance=data)
    #     return render(request, template_name=self.template_name, context={'data': data, 'formset': formset})



class TestAdd(View):
    model = Test_Model
    template_name = 'test_model_list.html'
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
