from django.shortcuts import render,redirect
from .models import Activity

# Create your views here.

def activities_list(request):
    activities = Activity.objects.all().order_by('-date')# fetch activities sorted by date
    return render(request, 'activities.html', {'activities':activities})