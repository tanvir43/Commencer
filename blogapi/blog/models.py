from django.db import models
from django.contrib.auth.models import User


class PostManager(models.Manager):
    def published(self):
        return super().get_queryset().filter(created_at__isnull=False)


class Category(models.Model):
    name = models.CharField(max_length=50)


class Post(models.Model):
    
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = PostManager()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
