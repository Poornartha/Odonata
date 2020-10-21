from django.contrib import admin
<<<<<<< HEAD
from .models import Child, Emp, Parent, Project, Team, Voting
=======
from . models import Child, Emp, Parent, Project, Team, Voting, Organization
>>>>>>> 2af4b3450dc207096f6496a8e4608ec009973c72

# Register your models here.
admin.site.register(Organization)
admin.site.register(Child)
admin.site.register(Emp)
admin.site.register(Parent)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Voting)