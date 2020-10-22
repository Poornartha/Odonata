from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from Client.models import Project , Emp , Team , Parent , Child , Submission
from django.utils import timezone
import datetime

# Create your views here.


def create_project(request):
    context={}
    context['flag'] = False
    if request.method == 'POST':
        user = request.user
        project_name = request.POST['project_name']
        project_description = request.POST['project_description']
        default_points = request.POST['default_points']
        deadline = request.POST['deadline']
        Project.objects.create(name=project_name ,parent=user , description=project_description , default_pts=default_points , deadline=deadline)
        print('project created succesfully')
        context['flag'] = True
        return HttpResponseRedirect(reverse , 'create_project')
    else:
        print('project created unsuccessful')
    return render(request , 'projects/project_create.html' , context)

def submit_project(request , ppk ,tpk):
    context = {}
    context['flag'] = False
    project = Project.objects.get(id = ppk)
    team = Team.objects.get(id = tpk)
    user = request.user
    employee = Emp.objects.get(user = user)
    child = Child.objects.filter(emp=employee , parent=project.parent)
    if child in team.child.all():
        if request.method == 'POST':
            project_file = request.FILES['project_file']
            project.file_project = project_file
            timestamp = timezone.now
            after_deadline = False
            if timestamp > project.deadline :
                context['messages'] = 'You have submitted your project after deadline'
                after_deadline = True
            Submission.objects.create(project=project , child=child , team=team , after_deadline=after_deadline)
            return HttpResponseRedirect(reverse ,name = 'project_submit')
    return render(request , 'projects/project_submit.html',context)

def accept_project(request , ppk , tpk):
    context = {}
    user = request.user
    team =Team.objects.get(id = tpk)
    employee = Emp.objects.get(user=user)
    parent = Parent.objects.filter(emp = employee)
    #context['files'] = project.file_project.all()[0]
    leader = Project.objects.filter(id = ppk , parent=parent)
    context['childs'] = team.child.filter()
    print(accept_project,rejected_project , leader , team , employee)
    if leader is not None:
        if request.method == 'POST':
            accepted_project = request.POST['accepted_project']
            rejected_project = request.POST['rejected_project']
            print(accept_project,rejected_project , leader , team , employee)
            return HttpResponseRedirect(reverse , 'project_accept')
    else:
        context['messages'] = 'You are not authorized'
    return render(request , 'projects/project_accept.html' , context)
