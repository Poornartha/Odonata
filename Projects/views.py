from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from Client.models import Project , Emp , Team , Parent , Child , Submissions
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
    return render(request , 'project_create.html' , context)

def submit_project(request , ppk ,tpk):
    context = {}
    context['flag'] = False
    project = Project.objects.get(id = ppk)
    team = Teams.objects.get(id = tpk)
    user = request.user
    employee = Emp.objects.all(user = user)
    child = Child.objects.get(emp=employee , parent=project.parent)
    if child in team.child.all():
        if request.method == 'POST':
            project_file = request.FILES['project_file']
            project.file_project = project_file
            timestamp = datetime.now()
            after_deadline = False
            if timestamp > project.deadline :
                context['messages'] = 'You have submitted your project after deadline'
                after_deadline = True
            Submissions.objects.create(project=project , child=child , team=team , after_deadline=after_deadline)
            return HttpResponseRedirect(reverse ,name = 'project_submit')
    return render(request , 'project_submit',context)

def accept_project(request):
    pass
    return render(request , 'project_accept')
