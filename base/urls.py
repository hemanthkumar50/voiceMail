from django.urls import path
from .views import *

urlpatterns = [
    path("home/", home, name="home"),
    path("compose/", compose, name="compose"),
    path("doc/", doc, name="doc"),
    path("dupe/", dupe, name="dupe"),
    path("sent_preview/", sent_preview, name="sent_preview"),
    path("sent/", sent, name="sent"),
    path("view/", view, name="view"),
    path("voice/", voice, name="voice"),
 
]