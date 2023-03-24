from django.shortcuts import render

from blog.models import Blog, Category


def blogs(request):
    blogs = Blog.objects.all()
    cats = Category.objects.all()
    context = {"blogs": blogs, "cats": cats}

    return render(request, "blog/index.html", context)


def single_blog(request, slug):
    cats = Category.objects.all()

    blog = Blog.objects.get(slug=slug)
    blog.count = blog.count + 1
    blog.save()

    similar_blogs = Blog.objects.filter(category__name=blog.category).exclude(
        slug=blog.slug
    )
    context = {"blog": blog, "cats": cats, "similar_blogs": similar_blogs}
    return render(request, "blog/single_blog.html", context)


def get_category_objs(request, id):
    cats = Category.objects.all()
    cat_objs = Blog.objects.filter(category=id)
    context = {"cat_objs": cat_objs, "cats": cats}

    return render(request, "blog/category_blogs.html", context)


def about(request):
    cats = Category.objects.all()
    return render(request, "blog/about.html", {"cats": cats})
