from django.test import SimpleTestCase
from django.urls import resolve, reverse

from blog.views import about, blogs, get_category_objs, single_blog


class TestUrls(SimpleTestCase):
    def test_homepage_url_is_resolved(self):
        url = reverse("homepage")
        resolved_url = resolve(url)
        self.assertEqual(resolved_url.func, blogs)

    def test_single_blog_url_is_resolved(self):
        url = reverse("single-blog", args=["some-slug"])
        resolved_url = resolve(url)
        self.assertEqual(resolved_url.func, single_blog)

    def test_get_category_objs_url_is_resolved(self):
        url = reverse("category-objs", args=["1"])
        resolved_url = resolve(url)
        self.assertEqual(resolved_url.func, get_category_objs)

    def test_about_url_is_resolved(self):
        url = reverse("about")
        resolved_url = resolve(url)
        self.assertEqual(resolved_url.func, about)
