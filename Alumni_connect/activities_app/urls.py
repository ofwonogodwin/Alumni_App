from django.urls import path
from .views import activities_list

urlpatterns = [
    path('', activities_list,name='activities_list'),
]