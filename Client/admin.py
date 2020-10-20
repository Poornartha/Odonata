from django.contrib import admin
from .models import Child, Emp, Parent, Project, Team, Voting

# Register your models here.
admin.site.register(Child)
admin.site.register(Emp)
admin.site.register(Parent)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Voting)