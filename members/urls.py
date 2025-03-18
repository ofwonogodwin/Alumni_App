from django.urls import path
from . import views

app_name = 'members'
urlpatterns = [
    path('', views.member_list_view, name='member_list'),
    path('profile/<int:user_id>/', views.profile_view, name='profile'),  # View a profile
    path('profile/edit/', views.profile_edit_view, name='profile_edit'),
]