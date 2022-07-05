from django.db import models

from django.conf import settings


class Language(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Source(models.Model):
    name = models.CharField(max_length=100, unique=True)
    urls = models.CharField(max_length=150, unique=True)


class Books(models.Model):
    img = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=355)
    description = models.TextField(blank=True)
    tom_number = models.IntegerField()
    tom_name = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    book_status = models.ForeignKey('Status', on_delete=models.CASCADE)
    book_source = models.ForeignKey('Source', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category')
    authors = models.ManyToManyField('Author')


class Ratings(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book_id = models.ForeignKey('Books', on_delete=models.CASCADE)


class Chapters(models.Model):
    book_id = models.ForeignKey('Books', on_delete=models.CASCADE)
    chapter_number = models.IntegerField()
    chapter_name = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    prime = models.BooleanField(default=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    publish_at = models.DateTimeField()
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )





