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
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'country': forms.Select(attrs={'class': 'form-control'}),
        #     'city': forms.Select(attrs={'class': 'form-control'}),
        #     'hostname': forms.TextInput(attrs={'class': 'form-control'}),
        #     'gateway_info': forms.TextInput(attrs={'class': 'form-control'}),
        #     'local_ip': forms.TextInput(attrs={'class': 'form-control'}),
        #     'title_comment': forms.TextInput(attrs={'class': 'form-control'}),
        #     'officeIp1': forms.TextInput(attrs={'class': 'form-control'}),
        #     'officeIp2': forms.TextInput(attrs={'class': 'form-control'}),
        #     'officeIp3': forms.TextInput(attrs={'class': 'form-control'}),
        #     'officeIp4': forms.TextInput(attrs={'class': 'form-control'}),
        #     'client_status': forms.Select(attrs={'class': 'form-control'}),
        #     'local_ip': forms.TextInput(attrs={'class': 'form-control'}),
        #     'os_version': forms.TextInput(attrs={'class': 'form-control'}),
        #     'ast_version': forms.TextInput(attrs={'class': 'form-control'}),
        #     'login_ccs': forms.TextInput(attrs={'class': 'form-control'}),
        #     'secret_ccs': forms.TextInput(attrs={'class': 'form-control'}),
        #     'ccs_version': forms.TextInput(attrs={'class': 'form-control'}),
        #     'cphone_maxvers': forms.TextInput(attrs={'class': 'form-control'}),
        #     'additional_info': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        #     'date_on': forms.TextInput(attrs={'class': 'form-control'}),
        #     'date_off': forms.TextInput(attrs={'class': 'form-control'}),
        # }

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('country',)
        exclude = ()

        widgets = {
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ('country', 'city')
        exclude = ()

        # widgets = {
        #     'country': forms.Select(attrs={'class': 'form-control'}),
        #     'city': forms.TextInput(attrs={'class': 'form-control'}),
        # }

class Client_NumberForm(forms.ModelForm):
    class Meta:
        model = Client_Number
        fields = ('client', 'name', 'number', 'comment', 'hide')
        exclude = ()

        # widgets = {
        #     'client': forms.Select(attrs={'class': 'form-control'}),
        #     'name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'number': forms.TextInput(attrs={'class': 'form-control'}),
        #     'comment': forms.TextInput(attrs={'class': 'form-control'}),
        # }

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

        # widgets = {
        #     'client': forms.Select(attrs={'class': 'form-control'}),
        #     'ip': forms.TextInput(attrs={'class': 'form-control'}),
        #     'port': forms.TextInput(attrs={'class': 'form-control'}),
        # }

class Client_GatewaForm(forms.ModelForm):
    class Meta:
        model = Client_Gateway
        fields = ('client', 'ip', 'port', 'login', 'secret', 'type_gateway')
        exclude = ()

        # widgets = {
        #     'client': forms.Select(attrs={'class': 'form-control'}),
        #     'ip': forms.TextInput(attrs={'class': 'form-control'}),
        #     'port': forms.TextInput(attrs={'class': 'form-control'}),
        #     'login': forms.TextInput(attrs={'class': 'form-control'}),
        #     'secret': forms.TextInput(attrs={'class': 'form-control'}),
        #     'type_gateway': forms.Select(attrs={'class': 'form-control'}),
        # }


Ip_ListFormSet = inlineformset_factory(Client, Ip_List, form=Ip_ListForm,
                                       fields=('id', 'ip', 'port',), extra=1, can_delete=True)
Client_NumberFormSet = inlineformset_factory(Client, Client_Number, form=Client_NumberForm,
                                             fields=('id', 'client', 'name', 'number', 'comment', 'hide',), extra=1, can_delete=True)
Client_GatewayFormSet = inlineformset_factory(Client, Client_Gateway, form=Client_GatewaForm,
                                              fields=('id', 'ip', 'port', 'login', 'secret', 'type_gateway',), extra=1,
                                              can_delete=True)
