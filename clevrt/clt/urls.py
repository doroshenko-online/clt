"""clevrt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib.auth import views as auth_view
from . import views
from django.conf import settings
from django.conf.urls.static import static
import os
from django.views.decorators.csrf import csrf_exempt

app_name = 'clt'

urlpatterns = [
    #test main page
    path('', views.Index.as_view(), name='index'),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('clients/', views.Clients.as_view(), name='clients'),
    path('test/', views.Test.as_view(), name='test'),
    path('test2/', csrf_exempt(views.Test2.as_view()), name='test2'),
    path('client/add/', views.ClientCreate.as_view(), name='client-add'),
    path('client/change/<int:pk>', views.ClientUpdate.as_view(), name='client-change'),
    path('client/<int:pk>', views.ClientView.as_view(), name='client'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, "static"))
