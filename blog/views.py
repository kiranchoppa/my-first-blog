from django.shortcuts import render
from .models import Post, Person
from django.contrib.auth.models import User


# Create your views here.
def post_list(request):
    me = User.objects.get(username="kiran")
    posts = Post.objects.filter(author=me)
    return render(request, "blog/post_list.html", {"posts": posts})
