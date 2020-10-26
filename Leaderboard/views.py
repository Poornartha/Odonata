from django.shortcuts import render
from Client.models import Points, Emp, Organization
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your views here.


def weekly_lead(request):
    current = timezone.now()
    days = datetime.timedelta(days=7)
    user_points = {}
    user = request.user
    context = {}
    context['valid'] = True
    try:
        organization = Organization.objects.get(user=user)
    except:
        try:
            employee = Emp.objects.get(user=user)
            organization = employee.organization
        except:
            organization = None
    if organization:
        for user in User.objects.all():
            try:
                employee = Emp.objects.get(user=user)
            except:
                employee = None
            if employee:
                if user not in user_points.keys():
                    user_points[user] = 0
        for point in Points.objects.all():
            if point.reciever in user_points.keys():
                if current - point.timestamp < days: 
                    user_points[point.reciever] += point.points
        points_manager = []
        print(user_points)
        for key in user_points.keys():
            emp = Emp.objects.get(user=key)
            points_manager.append((emp, user_points[key]))
        points_manager.sort(key=lambda x: x[1])
        points_manager.reverse()
        context['points_manager'] = points_manager
        context['current'] = current
    else:
        context['valid'] = False
    return render(request, 'leaderboard/weekly_lead.html', context)


def yearly_lead(request):
    current = timezone.now()
    days = datetime.timedelta(days=365)
    user_points = {}
    user = request.user
    context = {}
    context['valid'] = True
    try:
        organization = Organization.objects.get(user=user)
    except:
        try:
            employee = Emp.objects.get(user=user)
            organization = employee.organization
        except:
            organization = None
    if organization:
        for user in User.objects.all():
            try:
                employee = Emp.objects.get(user=user)
            except:
                employee = None
            if employee:
                if user not in user_points.keys():
                    user_points[user] = 0
        for point in Points.objects.all():
            if point.reciever in user_points.keys():
                if current - point.timestamp < days: 
                    user_points[point.reciever] += point.points
        points_manager = []
        for key in user_points.keys():
            emp = Emp.objects.get(user=key)
            points_manager.append((emp, user_points[key]))
        points_manager.sort(key=lambda x: x[1])
        points_manager.reverse()
        context['points_manager'] = points_manager
        context['current'] = current
    else:
        context['valid'] = False
    return render(request, 'leaderboard/yearly_lead.html', context)


def quaterly_lead(request):
    current = timezone.now()
    days = datetime.timedelta(days=90)
    user_points = {}
    user = request.user
    context = {}
    context['valid'] = True
    try:
        organization = Organization.objects.get(user=user)
    except:
        try:
            employee = Emp.objects.get(user=user)
            organization = employee.organization
        except:
            organization = None
    if organization:
        for user in User.objects.all():
            try:
                employee = Emp.objects.get(user=user)
            except:
                employee = None
            if employee:
                if user not in user_points.keys():
                    user_points[user] = 0
        for point in Points.objects.all():
            if point.reciever in user_points.keys():
                if current - point.timestamp < days: 
                    user_points[point.reciever] += point.points
        points_manager = []
        for key in user_points.keys():
            emp = Emp.objects.get(user=key)
            points_manager.append((emp, user_points[key]))
        points_manager.sort(key=lambda x: x[1])
        points_manager.reverse()
        context['points_manager'] = points_manager
        context['current'] = current
    else:
        context['valid'] = False
    return render(request, 'leaderboard/quaterly_lead.html', context)