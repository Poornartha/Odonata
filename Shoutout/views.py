from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from Client.models import Project , Child , Parent , Team , Emp , Organization , Voting , User
from Shoutout.models import Shoutout , Comment
import datetime
from Organization.urls import org_login
from Candidate.urls import emp_login
# Create your views here.

def shoutout_create(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        organization = Organization.objects.get_or_create(user= user)
        employee = Emp.objects.get(user = user)
        employees = Emp.objects.filter(organization=employee.organization.id)
        context['user_name'] = employee.name
        employee_list = []
        print(employee.organization.id)
        for employee in employees.all():
            employee_list.append(employee)
        context['employees'] = employee_list
        shoutouts = Shoutout.objects.all().order_by('-timestamp')
        print(shoutouts)
        shoutout_list = []
        if shoutouts:
            for shoutout in shoutouts:
                print(shoutout.emp_appreciated)
                shoutout_list.append(shoutout)
            context['shoutouts'] = shoutout_list
        print(shoutout_list,user)
        if request.method =="POST":
            employee_name = request.POST['employee_name']
            employee_appreciated = Emp.objects.get(name=employee_name , organization=employee.organization.id)
            description = request.POST['description']
            timestamp = datetime.datetime.now()
            points = request.POST['points']
            if points != '':
                if int(points) < employee.points:
                    employee.points -= int(points)
                    employee_appreciated.points += int(points)
                    employee.save()
                    employee_appreciated.save()
                else:
                    context['messages'] = 'You do not have sufficient points'
            Shoutout.objects.create(emp_appreciated=employee_appreciated , emp_appreciator=user ,description=description , timestamp=timestamp)
            print('Shoutout created')
            return HttpResponseRedirect(reverse('shoutout_create'))
    else:
        return HttpResponseRedirect(reverse('emp_login'))
    return render(request , 'shoutouts/shoutout.html' , context)
