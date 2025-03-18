
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Activity

#@login_required
def activities_list(request):
    activities = Activity.objects.all().order_by('-date')# fetch activities sorted by date
    return render(request, 'activities.html', {'activities':activities})