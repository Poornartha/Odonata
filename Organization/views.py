from django.shortcuts import render
from Client.models import Organization, Child, Team, Emp, Project, Parent
from django.contrib.auth.models import User


# Create your views here.
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
                elif len(list(User.objects.all().filter(username=username))) > 0 :
                    context['message'] = "Organization with that username already exists."
                else:
                    user = User.objects.create(username=username, email=email, password=password)
                    organization = Organization.objects.create(name=user.username, description=description, user=user)
    else:
        context['valid1'] = False
    return render(request, 'organization/org_create.html', context)

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
        name = request.POST['name']
        
    return render(request, 'organization/team_create.html', context)