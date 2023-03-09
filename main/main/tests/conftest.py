from pytest_factoryboy import register

from .factories import BlogFactory, CategoryFactory

register(BlogFactory)
register(CategoryFactory)
