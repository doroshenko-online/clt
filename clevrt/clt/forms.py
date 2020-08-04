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

CFormSet = inlineformset_factory(Test_Model, Test_C, form=TestForm, extra=1)
