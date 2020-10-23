from django.urls import path
<<<<<<< HEAD
from .views import org_create, team_create, voting
=======
from .views import org_create, org_login, org_architecture, team_create
>>>>>>> dc0195a9e45a79f49bbeb60db6c4f3d6b0074db8


urlpatterns = [
    path('create/', org_create, name="org_create"),
    path('login/', org_login, name="org_login"),
    path('designation/', org_architecture, name="org_architecture"),
    path('team_create/<int:ppk>', team_create, name="team_create"),
<<<<<<< HEAD
    path('voting/<int:ppk>', voting, name="voting"),

=======
>>>>>>> dc0195a9e45a79f49bbeb60db6c4f3d6b0074db8
]