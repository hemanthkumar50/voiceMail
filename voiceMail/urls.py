"""
URL configuration for voiceMail project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from base.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home", home, name="home"),
    path("compose", compose, name="compose"),
    path("doc", doc, name="doc"),
    path("dupe", dupe, name="dupe"),
    path("sent_preview", sent_preview, name="sent_preview"),
    path("sent", sent, name="sent"),
    path("view", view, name="view"),
    path("voice", voice, name="voice"),
    path("vr", vr, name="vr"),
    
]
