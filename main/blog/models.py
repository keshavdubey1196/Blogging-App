from django.contrib.auth.models import User
from django.db import models
from froala_editor.fields import FroalaField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="blog_author",
    )
    content = FroalaField(default=None)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        default=None,
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
