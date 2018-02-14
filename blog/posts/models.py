from django.db import models
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateField(default=timezone.now)
    date_pub = models.DateField()
    date_mod = models.DateField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
