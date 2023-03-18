from django.urls import path

from . import views

urlpatterns = [
    path("", views.blogs, name="homepage"),
    path("contact/", views.contactUs, name="contact-us"),
    path("category/<str:id>/", views.get_category_objs, name="category-objs"),
    path("about/", views.about, name="about"),
    path(
        "single-blog/<slug:slug>/",
        views.single_blog,
        name="single-blog",
    ),
]
