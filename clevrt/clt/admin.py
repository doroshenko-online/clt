from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Ip_List)
admin.site.register(Client_Gateway)
admin.site.register(Client_Number)
admin.site.register(Log)
admin.site.register(Log_String)
admin.site.register(User_Setting)