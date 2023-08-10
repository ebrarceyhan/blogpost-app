from django.contrib import admin
from django.urls import path, include
from blogpost.views import home_view, category_view, post_detail_view


urlpatterns = [
    path("", home_view, name="home"),
    path("admin/", admin.site.urls),
    path("<slug:category_slug>/", category_view, name="category_view"),
    path("user/", include("user_profile.urls")),
    path(
        "<slug:category_slug>/<int:id>/",
        post_detail_view,
        name="post_detail_view",
    ),
]
