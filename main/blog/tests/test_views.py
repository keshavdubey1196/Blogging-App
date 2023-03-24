from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from blog.models import Blog, Category, Tag

BLOGS_LIST_URL = reverse("homepage")
CATEGORIES_URL = reverse("category-objs", args=["1"])
ABOUT_URL = reverse("about")


def detail_url(slug):
    # create and return a detail url
    return reverse("single-blog", args=[slug])


def create_category():
    cat1 = Category.objects.create(name="test_category")
    return cat1


def create_tag():
    tag1 = Tag.objects.create(name="test_tag")
    return tag1


def create_user(**params):
    return get_user_model().objects.create(**params)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        self.test_user = create_user(
            username="test_user",
            password="test_password",
        )

        # self.category1 = Category.objects.create(name="testCat")
        # self.tag1 = Tag.objects.create(name="testTag")

        self.blog1 = Blog.objects.create(
            title="testTitle",
            author=self.test_user,
            slug="test-slug",
            content="testcontent",
            category=create_category(),
        )

        self.blog1.tags.add(create_tag())

        # self.list_blog_url = reverse("homepage")
        # self.single_blog_url = reverse("single-blog", args=["test-slug"])
        self.get_category_url = reverse("category-objs", args=["1"])
        self.about_url = reverse("about")

    def test_blogs_view(self):
        response = self.client.get(BLOGS_LIST_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")

    def test_single_blog_view(self):
        response = self.client.get(detail_url("test-slug"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/single_blog.html")

    def test_get_category_view(self):
        response = self.client.get(CATEGORIES_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/category_blogs.html")

    def test_about_view(self):
        response = self.client.get(ABOUT_URL)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/about.html")
