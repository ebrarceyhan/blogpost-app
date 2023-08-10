from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from blogpost.models import Post, Category


def home_view(request):
    posts = Post.objects.filter(is_deleted=False)
    context = dict(posts=posts)
    return render(request, "blogpost/postlist.html", context)


@login_required(login_url="/admin/login/")
def category_view(
    request,
    category_slug,
):
    category = get_object_or_404(Category, slug=category_slug)
    blogs = Post.objects.filter(category=category)
    context = dict(
        category=category,
        blogs=blogs,
    )
    return render(request, "blogpost/postlist.html", context)


@login_required(login_url="/admin/login/")
def post_detail_view(request, category_slug, id):
    item = get_object_or_404(Post, pk=id)
    context = dict(
        item=item,
    )
    return render(request, "blogpost/postdetail.html", context)


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user != post.user:
        return redirect("/")
    if request.method == "POST":
        context = {"post": post}
    return render(request, "edit_post.html", context)
