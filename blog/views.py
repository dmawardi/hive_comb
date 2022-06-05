from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import date

# Import model for query
from .models import Author, Project_post, Tag

# Create your views here.


def index(request):
    # Django automatically filters only 3 items ordered by date in desc order
    latest_projects = Project_post.objects.all().order_by("-date")[:3]
    # Uses get_date to sort the posts by date
    # sorted_projects = sorted(all_projects, key=get_date)
    return render(request, "blog/index.html", {
        "latest_projects": latest_projects
    })


def projects(request):
    all_projects = Project_post.objects.all().order_by("-date")

    return render(request, "blog/projects-home.html", {
        "projects": all_projects
    })


def project_detail(request, slug):
    # project = Project_post.objects.get(slug=slug)
    project = get_object_or_404(Project_post, slug=slug)

    return render(request, "blog/project-post.html", {
        "slug": slug,
        "project": project,
        # To access many to many relationship, you need to query using .all
        "project_tags": project.tags.all()
    })
