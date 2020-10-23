from django.shortcuts import render, redirect, reverse
from Client.models import Organization
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





