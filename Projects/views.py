from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from Client.models import Project , Emp , Team , Parent , Child , Submission, Points, ParentProject
from django.utils import timezone
import datetime
from Organization.urls import team_create
from Candidate.urls import emp_login
# Create your views here.

def create_project(request):
    context={}
    context['flag'] = False
    user = request.user
    organization = Emp.objects.get(user=user).organization
    parent_projects = ParentProject.objects.all()
    emp = Emp.objects.get(user=user)
    parent = Parent.objects.get(emp=emp)
    print(parent)
    teams = parent.team_set.all()
    # pp = []
    # for team in teams:
    #     for project in Project.objects.all().filter(team=team):
    #         pp.append(project.parentproject)
    # parent_projects = set(pp)
    context['parent_projects'] = parent_projects
    teams = Team.objects.all()
    context['teams'] = teams
    if request.method == 'POST':
        user = request.user
        project_name = request.POST['project_name']
        project_description = request.POST['project_description']
        # default_points = request.POST['default_points']
        deadline = request.POST['deadline']
        # c_points = request.POST['c_points']
        # b_points = request.POST['b_points']

        # Functional Point
        wtFactor = [
            [3, 4, 6],
            [4, 5, 7],
            [3, 4, 6],
            [7, 10, 15],
            [5, 7, 10]
        ]

        ufp = 0

        cand1 = ["item1", "item2", "item3", "item4", "item5"]
        btns = ["radio1", "radio2", "radio3"]

        for cand_index in range(len(cand1)):
            cand = cand1[cand_index]
            for j in range(3):
                check = cand + "-" + btns[j]
                try:
                    if request.POST[check]:
                        ufp += int(request.POST[cand]) * wtFactor[cand_index][j]
                except: 
                    pass
        
        q = ["q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "q11", "q12", "q13", "q14"]
        btns = ["radio1", "radio2", "radio3", "radio4", "radio5"]

        fi = 0

        for i in q:
            for j in btns:
                search = i + "-" + j
                try:
                    fi += int(request.POST[search])
                except:
                    pass
        
        caf = 0.65 + (0.01 * fi)
        fp = ufp * caf

        default_points = fp * 100
        c_points = 0
        b_points = 0

        print(fp)

        parent_project_name = request.POST['parent_project']
        timestamp = datetime.datetime.now()
        parent_project = ParentProject.objects.get(name=parent_project_name, organization=organization)
        team_name = request.POST['team']
        print(team_name)
        team = Team.objects.get(name=team_name)
        project_file = request.POST['project_file']
        total_points = int(default_points)+int(c_points)+int(b_points)
        employee = Emp.objects.get(user=user)
        parent , created = Parent.objects.get_or_create(emp=employee)
        project = Project.objects.create(team=team, parentproject=parent_project, name=project_name, c_pts=c_points , b_pts= b_points ,parent=parent , description=project_description , default_pts=default_points , deadline=datetime.datetime.strptime(deadline, '%Y-%m-%dT%H:%M') , timestamp = timestamp , project_create_file = project_file , total=total_points)
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
            Submission.objects.create(project=project , child=child , team=team , after_deadline=after_deadline , file_project = project_file , timestamp=timestamp)
            context['flag'] = True
            print('Submission successful')
            return HttpResponseRedirect(reverse('assigned_project'))
        else:
            print('not submitted')
    else:
        print('Not a child of that team')
    return render(request , 'projects/project_submit.html',context)

def accept_project(request , ppk , cpk):
    context = {}
    user = request.user
    project = Project.objects.get(id = ppk)
    child =Child.objects.get(id = cpk)
    employee = Emp.objects.get(user=user)
    parent = Parent.objects.filter(emp = employee)
    submissions = Submission.objects.filter(project = project , child = child)
    leader = Project.objects.filter(id = ppk , parent=parent)
    files_list = []
    for submission in submissions:
        if submission.file_project:
            files_list.append(submission.file_project)
        else:
            files_list=[]
    context['files'] = files_list
    context['child'] = child
    context['project'] = project
    if submissions:
        context['after_deadline'] = submissions[0].after_deadline
    else:
        context['after_deadline'] = True
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
                    try:
                        for sub in submission:
                            sub.status = True
                            sub.save()
                        print('Accepted')  
                    except:
                        submission.status = True
                        submission.save() 
                try:
                    if accepted_project == 'off':
                        for sub in submission:
                            sub.status = False
                            sub.save()
                        print('rejected')
                except:
                    pass
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
        complete_list = []
        incomplete_list = []
        for parent in parents:
            project = Project.objects.filter(parent=parent)
            for proj in project:
                if proj.status:
                    complete_list.append(proj)
                else:
                    incomplete_list.append(proj)
            context['complete_project'] = complete_list
            context['incomplete_project'] = incomplete_list
    return render(request , 'projects/project_display.html' , context)

def list_project(request , ppk):
    context = {}
    user = request.user
    employee = Emp.objects.get(user = user)
    parent = Parent.objects.filter(emp=employee).first()
    project = Project.objects.get(id = ppk , parent=parent)
    print(project.status)
    context['project'] = project
    context['teams'] = project.team
    if parent is project.parent:
        context['parent_status'] = True
    if project.status:
        pass
    else:
        context['project_status'] = True
    if request.method == 'POST':
            status = request.POST['status']
            if status == 'on':
                project.status = True
            else:
                project.status = False
            project.save()
            return HttpResponseRedirect(reverse('display_project'))
    return render(request , 'projects/project_list.html',context)

def assigned_project(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        employee = Emp.objects.get(user=user)
        children = Child.objects.filter(emp=employee)
        complete_list = []
        incomplete_list = []
        print(employee , children)
        for child in children.all():
            teams = Team.objects.filter(child=child)
            for team in teams.all():
                projects = Project.objects.filter(team=team)
                for project in projects:
                    submissions = Submission.objects.filter(child = child , team = team , project = project).order_by('-timestamp').first()
                    if submissions:
                        if submissions.status:
                            complete_list.append((submissions,project))
                        else:
                            incomplete_list.append((submissions,project))
                    else:
                        incomplete_list.append((submissions,project))
                context['completed'] = complete_list
                context['incompleted'] = incomplete_list
        print(complete_list , incomplete_list)
    else:
        return HttpResponseRedirect(reverse('emp_login'))
    return render(request , 'projects/project_child.html' , context)
