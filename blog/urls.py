from django.urls import path
from . import views

# List of url patterns
urlpatterns = [
    path("", views.index, name="index"),
    path("projects/", views.projects,
         name="projects-home"),
    # dynamic path with parameter. Allows for type casting
    path("projects/<slug:blogId>", views.project_detail,
         name="project-detail")


]
