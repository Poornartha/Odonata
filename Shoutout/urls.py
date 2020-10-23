from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from .views import shoutout_create

urlpatterns = [
    path('' , shoutout_create , 'shoutout_create'),
]