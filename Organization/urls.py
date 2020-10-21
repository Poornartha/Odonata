from django.urls import path
from .views import org_create


urlpatterns = [
    path('create/', org_create, name="rog_create"),
]