from django.db import models
from django.contrib.auth.models import User


class Emp(models.Model):
    name = models.CharField(max_length= 50)
    doj = models.DateTimeField(auto_now_add = True)
    age = models.IntegerField()
    emp = models.OneToOneField(User,on_delete = models.CASCADE)
    points = models.IntegerField()
    designtion = models.CharField(max_length=20)
    def str(self):
        return self.name

class Parent(models.Model):
    emp = models.OneToOneField(Emp, on_delete = models.CASCADE)


class Child(models.Model):
    emp = models.ForeignKey(Emp, on_delete = models.CASCADE)
    parent = models.OneToOneField(Parent, on_delete = models.CASCADE)

class Project(models.Model):
    description = models.CharField(max_length=500)
    file_project = models.FileField(upload_to = 'files/', blank =True, null = True)
    default_pts = models.IntegerField()
    c_pts = models.IntegerField()
    b_pts = models.IntegerField()
    total = models.IntegerField()
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE)
    status = models.BooleanField()

class Team(models.Model):
    project = models.OneToOneField(Project, on_delete = models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE)
    child = models.ManyToManyField(Child)
    name = models.CharField(max_length=50)

    def str(self):
        return self.name

class Voting(models.Model):
    emp = models.OneToOneField(Emp, on_delete = models.CASCADE )
    team = models.OneToOneField(Team, on_delete = models.CASCADE)
    project = models.OneToOneField(Project, on_delete = models.CASCADE)
    total_pts = models.IntegerField()