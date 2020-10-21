from django.urls import path
from .views import org_create, team_create


urlpatterns = [
    path('create/', org_create, name="rog_create"),
    path('team_create/', team_create, name="team_create"),

]