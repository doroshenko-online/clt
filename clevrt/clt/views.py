from django.shortcuts import render, HttpResponse
from .models import *
from django.contrib.auth.models import *
import time
import datetime

# Create your views here.

def index(request):
    clients = Client.objects.all()
    return HttpResponse(request)