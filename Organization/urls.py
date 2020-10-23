from django.urls import path
from .views import org_create, org_login, org_architecture


urlpatterns = [
    path('create/', org_create, name="org_create"),
    path('login/', org_login, name="org_login"),
    path('designation/', org_architecture, name="org_architecture"),
]