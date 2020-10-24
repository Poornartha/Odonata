from django.urls import path


from .views import org_login, org_architecture, team_create,  voting


urlpatterns = [
    path('create/', org_create, name="org_create"),
    path('login/', org_login, name="org_login"),
    path('designation/', org_architecture, name="org_architecture"),
    path('team_create/<int:ppk>', team_create, name="team_create"),

    path('voting/<int:ppk>', voting, name="voting"),


]