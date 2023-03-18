from django.contrib.auth.models import User
from django.db import models

# from django.urls import reverse
from froala_editor.fields import FroalaField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(null=True, blank=True, default="default.jpg")
    short_about = models.TextField(null=True, blank=True, default=None)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_author",
    )
    slug = models.SlugField(max_length=250, unique=True)
    content = FroalaField(default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=0)
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        default=None,
    )
    tags = models.ManyToManyField(Tag, default=None)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
