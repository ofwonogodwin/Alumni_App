from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

#@login_required
def news_list_view(request):
    posts = Post.objects.all()
    return render(request, 'news_list.html', {'news': posts})

