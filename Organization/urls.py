from django.urls import path
from .views import org_create, team_create, voting


urlpatterns = [
    path('create/', org_create, name="rog_create"),
    path('team_create/<int:ppk>', team_create, name="team_create"),
    path('voting/<int:ppk>', voting, name="voting"),

]