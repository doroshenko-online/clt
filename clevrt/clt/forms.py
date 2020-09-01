from django import forms
from .models import *
from django.forms import formset_factory, inlineformset_factory


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

class Client_NumberForm(forms.ModelForm):
    class Meta:
        model = Client_Number
        fields = '__all__'
        exclude = ()

class Ip_ListForm(forms.ModelForm):
    class Meta:
        model = Ip_List
        exclude = ()

class Client_GatewaForm(forms.ModelForm):
    class Meta:
        model = Client_Gateway
        exclude = ()


Ip_ListFormSet = inlineformset_factory(Client, Ip_List, form=Ip_ListForm,
                                       fields=('id', 'ip', 'port',), extra=1, can_delete=True)
Client_NumberFormSet = inlineformset_factory(Client, Client_Number, form=Client_NumberForm,
                                             fields=('id', 'client', 'name', 'number', 'comment',), extra=1, can_delete=True)
Client_GatewayFormSet = inlineformset_factory(Client, Client_Gateway, form=Client_GatewaForm,
                                              fields=('id', 'ip', 'port', 'login', 'secret', 'type_gateway',), extra=1,
                                              can_delete=True)
