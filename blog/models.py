from pyexpat import model
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, MaxLengthValidator


# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Project_post(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80, unique=True, db_index=True)
    image_name = models.CharField(max_length=80)
    date = models.DateField(auto_now=True)
    excerpt = models.CharField(max_length=200)
    content = models.TextField(
        validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="projects")
    tags = models.ManyToManyField(Tag, related_name="projects")

    def __str__(self) -> str:
        return f"{self.title}"

    # Allows us to override default save
    def save(self, *args, **kwargs):
        # Create slug before save using title
        self.slug = slugify(self.title)
        # Init super class and save using default save function
        super().save(*args, **kwargs)
