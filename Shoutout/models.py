from django.db import models
from django.contrib.auth.models import User
from Client.models import Emp
# Create your models here.

class Shoutout(models.Model):
    description = models.TextField(max_length=200)
    emp = models.ForeignKey(Emp , on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)