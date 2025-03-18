
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages

@login_required
def member_list_view(request):
    members = User.objects.all()  # Get all users
    return render(request, 'member_list.html', {'members': members})

@login_required
def profile_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profile_view.html', {'user': user, 'profile': profile})

@login_required
def profile_edit_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        full_name =request.POST.get('full_name')
        bio = request.POST.get('bio')
        graduation_year = request.POST.get('graduation_year')
        current_employer = request.POST.get('current_employer')
        profile_picture = request.FILES.get('profile_picture')

        profile.bio = bio
        if full_name:
            profile.full_name = full_name
        if graduation_year:
            profile.graduation_year = graduation_year
        if current_employer:
            profile.current_employer=current_employer
        if profile_picture:
            profile.profile_picture = profile_picture
        profile.save()
        return redirect('members:profile', user_id=request.user.id)
    return render(request, 'profile_edit.html', {'profile': profile})