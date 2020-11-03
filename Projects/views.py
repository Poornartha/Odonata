from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from Client.models import Project , Emp , Team , Parent , Child , Submission, Points, ParentProject
from django.utils import timezone
import datetime
from Organization.urls import team_create
# Create your views here.

def create_project(request):
    context={}
    context['flag'] = False
    user = request.user
    organization = Emp.objects.get(user=user).organization
    # parent_projects = ParentProject.objects.all().filter(organization=organization)
    emp = Emp.objects.get(user=user)
    child = Child.objects.get(emp=emp)
    teams = child.team_set.all()
    pp = []
    for team in teams:
        for project in Project.objects.all().filter(team=team):
            pp.append(project.parentproject)
    parent_projects = set(pp)
    context['parent_projects'] = parent_projects
    teams = Team.objects.all().filter(organization=organization)
    context['teams'] = teams
    if request.method == 'POST':
        user = request.user
        project_name = request.POST['project_name']
        project_description = request.POST['project_description']
        default_points = request.POST['default_points']
        deadline = request.POST['deadline']
        c_points = request.POST['c_points']
        b_points = request.POST['b_points']
        parent_project_name = request.POST['parent_project']
        parent_project = ParentProject.objects.get(name=parent_project_name, organization=organization)
        team_name = request.POST['team']
        print(team_name)
        team = Team.objects.get(name=team_name)
        project_file = request.POST['project_file']
        total_points = int(default_points)+int(c_points)+int(b_points)
        employee = Emp.objects.get(user=user)
        parent , created = Parent.objects.get_or_create(emp=employee)
        project = Project.objects.create(team=team, parentproject=parent_project, name=project_name, c_pts=c_points , b_pts= b_points ,parent=parent , description=project_description , default_pts=default_points , deadline=datetime.datetime.strptime(deadline, '%Y-%m-%dT%H:%M') , project_create_file = project_file , total=total_points)
        print('project created succesfully')
        context['flag'] = True
        print(parent.emp.points , total_points)
        parent.emp.points -= total_points
        parent.emp.save()
        return HttpResponseRedirect(reverse('home'))
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
    child = Child.objects.get(emp=employee)
    if child in team.child.all():
        if request.method == 'POST':
            project_file = request.FILES['project_file']
            print(project_file)
            timestamp = datetime.datetime.now().date()
            after_deadline = False
            if timestamp > project.deadline:
                context['messages'] = 'You have submitted your project after deadline'
                after_deadline = True
            Submission.objects.create(project=project , child=child , team=team , after_deadline=after_deadline , file_project = project_file)
            context['flag'] = True
            print('Submission successful')
            return HttpResponseRedirect(reverse('list_project', args=[str(ppk)]))
        else:
            print('not submitted')
    else:
        print('Not a child of that team')
    return render(request , 'projects/project_submit.html',context)

def accept_project(request , ppk , cpk):
    context = {}
    checksum = 0
    user = request.user
    project = Project.objects.get(id = ppk)
    child =Child.objects.get(id = cpk)
    employee = Emp.objects.get(user=user)
    parent = Parent.objects.filter(emp = employee)
    submission = Submission.objects.filter(project = project , child = child)
    leader = Project.objects.filter(id = ppk , parent=parent)
    files_list = []
    for sub in submission:
        files_list.append(sub.file_project)
    context['files'] = files_list
    context['child'] = child
    if leader is not None:
        if user.is_active:
            if request.method == 'POST':
                try:
                    accepted_project = request.POST['accepted_project']
                except:
                    accepted_project = 'off'
                try:    
                    rejected_project = request.POST['rejected_project']
                except:
                    rejected_project = 'off'
                if accepted_project == 'on':
                    print(project.default_pts , child.emp.points)    
                    if project.checksum < 1:    
                        team = project.team
                        children_count = len(list(team.child.all()))
                        project.available_points = project.default_pts//children_count
                        project.checksum += 1
                    project.default_pts -= project.available_points
                    child.emp.points += project.available_points
                    Points.objects.create(sender=project.parent.emp.user, reciever=child.emp.user, points=project.available_points, project=project)
                    child.emp.save()
                    project.save()
                    print(project.default_pts , child.emp.points , project.available_points)
                    for sub in submission:
                        sub.status = True
                        sub.save()
                    print('Accepted')
                if accepted_project == 'off':
                    for sub in submission:
                        sub.status = False
                        sub.save()
                    print('rejected')
                return HttpResponseRedirect(reverse('display_project'))   
    else:
        context['messages'] = 'You are not authorized'
    return render(request , 'projects/project_accept.html' , context)

def display_project(request):
    context={}
    user = request.user
    if user.is_active:    
        employee = Emp.objects.get(user=user)
        parents = Parent.objects.filter(emp=employee)
        children = Child.objects.filter(emp = employee)
        emp = Emp.objects.get(user=user)
        child = Child.objects.get(emp=emp)
        teams = child.team_set.all()
        pp = []
        for team in teams:
            for project in Project.objects.all().filter(team=team):
                pp.append(project.parentproject)
            parent_projects = set(pp)
            context['projects_parents'] = []
        project_list_child = []
        for child in children:
            teams = Team.objects.filter(child = child)
            for team in teams:
                projects = Project.objects.filter(team = team)
                for project in projects:
                    project_list_child.append(project)
                    try:
                        submission = Submission.objects.get(child = child , team = team , project = project)
                    except:
                        submission = []
                context['projects_children'] = project_list_child
                # context['submissions'] = submission
    return render(request , 'projects/project_display.html' , context)

def list_project(request , ppk):
    context = {}
    user = request.user
    employee = Emp.objects.get(user = user)
    parent = Parent.objects.filter(emp=employee).first()
    try:
        project = Project.objects.get(id = ppk, parent = parent)
    except:
        project = None
    context['project'] = project
    if project:
        context['teams'] = project.team
        if parent is project.parent:
            context['parent_status'] = True
    return render(request , 'projects/project_list.html',context)