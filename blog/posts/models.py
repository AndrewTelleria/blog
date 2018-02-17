from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateField(default=timezone.now)
    date_pub = models.DateField(blank=True, null=True)
    date_mod = models.DateField(blank=True, null=True)
    

    def publish(self):
        self.date_pub = timezone.now()
        self.save()

    def __str__(self):
        return self.title
