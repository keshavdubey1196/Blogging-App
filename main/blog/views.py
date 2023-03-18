from django.shortcuts import render

from blog.models import Blog, Category


def blogs(request):
    blogs = Blog.objects.all()
    cats = Category.objects.all()
    context = {"blogs": blogs, "cats": cats}

    return render(request, "blog/index.html", context)


def single_blog(request, slug):
    blog = Blog.objects.get(slug=slug)
    blog.count = blog.count + 1
    blog.save()
    cats = Category.objects.all()
    context = {"blog": blog, "cats": cats}
    return render(request, "blog/single_blog.html", context)


def contactUs(request):
    return render(request, "blog/contact_form.html")


def get_category_objs(request, id):
    cats = Category.objects.all()
    cat_objs = Blog.objects.filter(category=id)
    context = {"cat_objs": cat_objs, "cats": cats}

    return render(request, "blog/category_blogs.html", context)


def about(request):
    return render(request, "blog/about.html")
