from django.urls import path

from .views import shoutout_create



urlpatterns = [
    path('shoutout_create/', shoutout_create, name="shoutout_create"),
    
]