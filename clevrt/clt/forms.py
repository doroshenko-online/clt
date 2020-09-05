from django import forms
from .models import *
from django.forms import formset_factory, inlineformset_factory
from django.core.exceptions import ValidationError


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name','country', 'city', 'hostname', 'gateway_info', 'local_ip', 'title_comment', 'officeIp1', 'officeIp2', 'officeIp3', 
        'officeIp4', 'client_status', 'os_version', 'ast_version', 'login_ccs', 'secret_ccs', 'ccs_version', 'cphone_maxvers', 'vps_own',
         'hide', 'additional_info', 'date_on', 'date_off')
        exclude = ()

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('country',)
        exclude = ()

class Client_NumberForm(forms.ModelForm):
    class Meta:
        model = Client_Number
        fields = ('client', 'name', 'number', 'comment', 'hide')
        exclude = ()

    def clean_number(self):
        number = self.cleaned_data['number']
        data = Client_Number.objects.exclude(client=self.cleaned_data['client']).filter(number=number)
        if data:
            raise ValidationError('Номер {0} уже закпреплен за клиентом {1}'.format(str(number), str(data[0].client.name)))
        return number


class Ip_ListForm(forms.ModelForm):
    class Meta:
        model = Ip_List
        fields = ('ip', 'port', 'client')
        exclude = ()

class Client_GatewaForm(forms.ModelForm):
    class Meta:
        model = Client_Gateway
        fields = ('client', 'ip', 'port', 'login', 'secret', 'type_gateway')
        exclude = ()


Ip_ListFormSet = inlineformset_factory(Client, Ip_List, form=Ip_ListForm,
                                       fields=('id', 'ip', 'port',), extra=1, can_delete=True)
Client_NumberFormSet = inlineformset_factory(Client, Client_Number, form=Client_NumberForm,
                                             fields=('id', 'client', 'name', 'number', 'comment', 'hide',), extra=1, can_delete=True)
Client_GatewayFormSet = inlineformset_factory(Client, Client_Gateway, form=Client_GatewaForm,
                                              fields=('id', 'ip', 'port', 'login', 'secret', 'type_gateway',), extra=1,
                                              can_delete=True)
