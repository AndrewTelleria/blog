from django.shortcuts import render, get_object_or_404
from .models import Post, Author
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(date_pub__lte=timezone.now()).order_by('date_pub')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

def post_new(request):
    p_form = PostForm()
    a_form = AuthorForm()
    return render(request, 'posts/post_edit.html',
            {'p_form': p_form,
             'a_form': a_form,
             }
        )
