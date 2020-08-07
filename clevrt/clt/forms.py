from django import forms
from .models import *
from django.forms import formset_factory, inlineformset_factory
from django.forms.models import BaseInlineFormSet

class TestForm(forms.ModelForm):
    class Meta:
        model = Test_Model
        fields = '__all__'
        exclude = ()


ChildFormSet = inlineformset_factory(Test_Model, Test_Child, form=TestForm, extra=1)
CFormSet = inlineformset_factory(Test_Model, Test_C, form=TestForm, extra=2)


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ()


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'
        exclude = ()


Ip_ListFormSet = inlineformset_factory(Client, Ip_List, form=ClientForm, extra=1)
Client_NumberFormSet = inlineformset_factory(Client, Client_Number, form=ClientForm, extra=1)
Client_GatewayFormSet = inlineformset_factory(Client, Client_Gateway, form=ClientForm, extra=1)
CCSFormSet = inlineformset_factory(Client, CCS, form=ClientForm, extra=1, max_num=1)
