from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "blog/index.html")


def projects(request):
    return render(request, "blog/projects-home.html")


def project_detail(request, blogId):
    return render(request, "blog/project-post.html", {
        "blogId": blogId,
    })
