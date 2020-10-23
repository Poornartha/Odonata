from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from .views import create_project , submit_project , accept_project


urlpatterns = [
    path('create/' , create_project , name = 'create_project'),
    path('<int:ppk>/<int:tpk>/submit/' , submit_project , name = 'submit_project'),
    path('<int:ppk>/<int:tpk>/accept/' , accept_project , name = 'accept_project')
]