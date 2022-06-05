from django.contrib import admin
from blog.models import Author, Tag, Project_post

# Register your models here.


class ProjectPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "date", "author", "slug",)
    list_filter = ("author", "tags",)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")


admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Project_post, ProjectPostAdmin)
