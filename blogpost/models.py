from django.contrib.auth.models import User
from django.urls import reverse as url
from django.db import models
from slugify import slugify


class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    def get_absolute_url(self):
        return url(
            "category_view",
            kwargs={"category_slug": self.slug},
        )


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to="post_images/", blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return url(
            "post_detail_view",
            kwargs={
                "category_slug": self.category.slug,
                "id": self.pk,
            },
        )
