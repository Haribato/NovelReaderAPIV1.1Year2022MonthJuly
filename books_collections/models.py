from django.db import models
from django.conf import settings


class TypeBookmarks(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    notify = models.BooleanField(default=True)
    notify_prime = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Bookmarks(models.Model):
    type_bookmarks_id = models.ForeignKey('TypeBookmarks', on_delete=models.CASCADE)
    book_id = models.ForeignKey(settings.BOOKS_MODEL, on_delete=models.CASCADE)
    passed_chapter_id = models.ForeignKey(settings.CHAPTERS_MODEL, on_delete=models.CASCADE)

    # def __str__(self):
    #