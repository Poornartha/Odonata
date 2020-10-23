from django.shortcuts import render, redirect, reverse
from Client.models import Organization
from django.shortcuts import render
from Client.models import Organization, Child, Team, Emp, Project, Parent, Voting, Voting_Points
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import Designation


# Create your views here.

def org_login(request):
    user = request.user
    context = {}
    context['valid1'] = True
    if not user.is_active:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
            else:
                context['message'] = "Please check you Username / Password and Try Again"
    else:
        context['valid1'] = False
    return render(request, 'organization/org_login.html', context)


def org_create(request):
    user = request.user
    context = {}
    context['valid1'] = True
    if not user.is_active:
        if request.method == "POST":
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['pass2']
            description = request.POST['description']
            if password != password2:
                context['message'] = "Your Passwords Don't Match. Try Again."
            else:
                if username == '' or email == '' or password == '':
                    context['message'] = "Fields aren't filled properly. Please Try again"
                elif len(list(User.objects.all().filter(username=username))) > 0 or len(list(User.objects.all().filter(email=email))) > 0 :
                    context['message'] = "Organization with that username already exists."
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    organization = Organization.objects.create(name=user.username, description=description, user=user)
                    return redirect('org_login')
    else:
        context['valid1'] = False
    return render(request, 'organization/org_create.html', context)

def org_architecture(request):
    context = {}
    user = request.user
    organization = Organization.objects.get(user=user) or None
    print(organization.confirmed)
    if organization.confirmed == True and organization.desigset == False:
        context['valid'] = True
        if request.method == "POST":
            organization.desigset = True
            organization.save()
            for i in range(1, 11):
                try:
                    name = 'text-' + str(i)
                    desig = request.POST[name]
                    if desig != '':
                        Designation.objects.create(organization=organization, designation=desig, priority=i)
                except:
                    break
    else:
        if organization is None:
            context['invalid'] = True
        context['valid'] = False
    return render(request, 'organization/org_architecture.html', context)


def team_create(request , ppk):
    context = {}

    
    project = Project.objects.get(id = ppk)
    context['project'] = project
    user = request.user
    employee = Emp.objects.get(user = user)
    parent = Parent.objects.get(emp = employee)
    children = Child.objects.filter(parent = parent)
    context['children'] = children
    if request.method == 'POST':
        
<<<<<<< HEAD
        team_name = request.POST['team_name']
      
        name1 = request.POST['name1']
        name2 = request.POST['name2']
        name3 = request.POST['name3']
        name4 = request.POST['name4']

        team =  Team.objects.create(name=team_name, parent = parent)
        team.child.add(name1)
        team.child.add(name2)
        team.child.add(name3)
        team.child.add(name4)
           
    return render(request, 'organization/team_create.html', context)



def voting(request, ppk):
    
    context = {}
    context['valid'] = False
    
    
    user = request.user
    
    employee = Emp.objects.get(user = user)
    child = Child.objects.get(emp = employee)
    project = Project.objects.get(id = ppk)
    team = project.team
    children = team.child.all()
   
    valid_children = []
    for c in children:
        
        if c != child:       
            valid_children.append(c)

    employee1 = valid_children[0].emp
    employee2 = valid_children[1].emp
    #employee3 = valid_children[2].emp

    employee_list = []
    employee_list.append(employee1)
    employee_list.append(employee2)
    #employee_list.append(employee3)

    context['employee_list'] = employee_list
    
    

    if project.status:
        context['valid'] = True
        if request.method == "POST":

            rank_1 = request.POST['rank_1']
            rank_2 = request.POST['rank_2']
            rank_3 = request.POST['rank_3']
            checksum = request.POST['checksum']
            print(checksum)
         
            voting_pts, created = Voting_Points.objects.get_or_create(project = project, employee = employee)
            



            

           

         


            

            
            
           
            
            
            

            

                    

    return render(request, 'organization/voting.html', context )

=======
    return render(request, 'organization/team_create.html', context)
>>>>>>> dc0195a9e45a79f49bbeb60db6c4f3d6b0074db8
