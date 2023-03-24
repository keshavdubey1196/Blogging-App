import factory
from django.contrib.auth.models import User

from blog import models


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = "testUser"
    password = "testpass123"
    is_superuser = True
    is_staff = True


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = "testCategory"


class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Blog

    title = "x"
    slug = "x"
    author = factory.SubFactory(UserFactory)
    content = "x"
    category = factory.SubFactory(CategoryFactory)


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Tag

    name = "testTag"
