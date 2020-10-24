from django.db import models
from Client.models import Emp, Project, Team

class Voting(models.Model):
    employee = models.ForeignKey(Emp, on_delete=models.CASCADE, related_name="employee")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team")
    rank = models.IntegerField(default=0)

class Votechecksum(models.Model):
    vote = models.OneToOneField(Voting, on_delete=models.CASCADE)
    checksum = models.IntegerField(default=0)


