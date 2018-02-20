from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_mod = models.DateTimeField(blank=True, null=True)
    date_pub = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.date_pub = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('posts.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.author
