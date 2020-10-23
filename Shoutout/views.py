from django.shortcuts import render
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from Client.models import Project , Child , Parent , Team , Emp , Organization , Voting , User
from Shoutout.models import Shoutout
# Create your views here.

def shoutout_create(request):
    context = {}
    pass
    return render(request , 'shoutout.html' , context)
