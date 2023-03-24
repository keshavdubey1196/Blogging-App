import pytest

pytestmark = pytest.mark.django_db


class TestBlogModel:
    def test_str_return(self, blog_factory):
        blog = blog_factory(title="test_blog")
        assert blog.__str__() == "test_blog"


class TestCategoryModel:
    def test_str_return(self, category_factory):
        category = category_factory(name="test_category")
        assert category.__str__() == "test_category"


class TestTagModel:
    def test_str_return(self, tag_factory):
        tag = tag_factory(name="test_tag")
        assert tag.__str__() == "test_tag"
