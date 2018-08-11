"""sosio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from splitmoney.views import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', admin.site.urls),
    url(r'^detail/$', Personal1), #mapping to individual views for expense details
    url(r'^addbill/$', Personal2),
    url(r'^dashboard/$', Dashboard),
    url(r'^bootstrap/$', TemplateView.as_view(template_name="bootstrap/example.html")), #screen to show who owe who
]