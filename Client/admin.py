from django.contrib import admin
<<<<<<< HEAD
from . models import Child, Emp, Parent, Project, Team, Voting, Organization, Voting_Points
=======
from . models import Child, Emp, Parent, Project, Team, Voting, Organization , Submission
>>>>>>> b6adaa3c9f4d5fbd74f55a2f3fc62f12f67afd8b

# Register your models here.
admin.site.register(Organization)
admin.site.register(Child)
admin.site.register(Emp)
admin.site.register(Parent)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Voting)
<<<<<<< HEAD
admin.site.register(Voting_Points)
=======
admin.site.register(Submission)
>>>>>>> b6adaa3c9f4d5fbd74f55a2f3fc62f12f67afd8b
