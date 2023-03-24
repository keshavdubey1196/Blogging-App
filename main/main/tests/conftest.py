from pytest_factoryboy import register

from .factories import BlogFactory, CategoryFactory, TagFactory

register(BlogFactory)
register(CategoryFactory)
register(TagFactory)
