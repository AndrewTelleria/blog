from django.shortcuts import render
from .models import Post, Author
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(date_pub__lte=timezone.now()).order_by('date_pub')
    return render(request, 'posts/post_list.html', {'posts': posts})
