from django.db import models
from django.conf import settings


class Posts(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_id = models.ForeignKey(settings.BOOKS_MODEL, on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['time_update']


class Comment(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_id = models.ForeignKey('Posts', on_delete=models.CASCADE)
    body = models.TextField(blank=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['time_update']
