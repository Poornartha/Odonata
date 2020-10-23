from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=100, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirmed = models.BooleanField(default=False, editable=True)
    desigset = models.BooleanField(default=False, editable=True)

    def __str__(self):
        return self.name

class Designation(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    designation = models.TextField()
    priority = models.IntegerField()

    def __str__(self):
        return self.designation

class Emp(models.Model):
    name = models.CharField(max_length= 50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE , default='')
    doj = models.DateTimeField(auto_now_add = True)
    dob = models.DateTimeField()
    age = models.IntegerField()
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    points = models.IntegerField()
    designation = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class Parent(models.Model):
    emp = models.OneToOneField(Emp, on_delete = models.CASCADE)

    def __str__(self):
        return self.emp.name


class Child(models.Model):
    emp = models.OneToOneField(Emp, on_delete = models.CASCADE)
    parent = models.ManyToManyField(Parent, blank=True)

    def __str__(self):
        return self.emp.name


class Team(models.Model):
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE)
    child = models.ManyToManyField(Child)
    name = models.CharField(max_length=50)

    def str(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=20 , blank=True , null=True)
    description = models.CharField(max_length=500)
    default_pts = models.IntegerField()
    project_create_file = models.FileField(upload_to='project_create/' , blank=True , null=True)
    c_pts = models.IntegerField()
    b_pts = models.IntegerField()
    total = models.IntegerField()
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE)
    status = models.BooleanField(default=False)
    deadline = models.DateField(blank=True , null=True)
    team = models.OneToOneField(Team, on_delete = models.CASCADE, null =True)
    checksum = models.IntegerField(default = 0)
    available_points = models.IntegerField(default = 0)


class Voting(models.Model):
    emp = models.OneToOneField(Emp, on_delete = models.CASCADE )
    team = models.OneToOneField(Team, on_delete = models.CASCADE)
    project = models.OneToOneField(Project, on_delete = models.CASCADE)
    total_pts = models.IntegerField()

class Submission(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    file_project = models.FileField(upload_to = 'files/', blank =True, null = True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    after_deadline = models.BooleanField(default=False)
<<<<<<< HEAD

class Voting_Points(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    employee = models.ForeignKey(Emp, on_delete = models.CASCADE)
    rank1 = models.IntegerField(default = 0)
    rank2 = models.IntegerField(default = 0)
    rank3 = models.IntegerField(default = 0)
    checksum = models.IntegerField(default = 0)
    
=======
    status = models.BooleanField(default=False , editable=True)
>>>>>>> b6adaa3c9f4d5fbd74f55a2f3fc62f12f67afd8b
