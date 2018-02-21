<<<<<<< HEAD
from django.contrib.auth.decorators import login_required
=======
<<<<<<< HEAD
from django.shortcuts import render, get_object_or_404
=======
>>>>>>> parent of 70f5b37... conflicts resolved
from django.shortcuts import render, get_object_or_404, redirect
>>>>>>> 7fb98766f5dbb77e4003ff5f56b114ec32fa665a
from .models import Post
from django.utils import timezone
from .forms import PostForm

<<<<<<< HEAD
=======
def post_list(request):
    posts = Post.objects.filter(date_pub__lte=timezone.now()).order_by('date_pub')
    return render(request, 'posts/post_list.html', {'posts': posts})

>>>>>>> parent of 70f5b37... conflicts resolved
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})

<<<<<<< HEAD

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(date_pub__isnull=True).order_by('date_created')
    return render(request, 'posts/post_draft_list.html', {'posts': posts})




@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
=======
def post_new(request):
>>>>>>> parent of 70f5b37... conflicts resolved
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
<<<<<<< HEAD
            post = p_form.save(commit=False)

        else:
            p_form = PostForm()
        # a_form = AuthorForm(request.POST)
    return render(request, 'posts/post_edit.html', {'form': form,})
=======
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form})

<<<<<<< HEAD

def post_list(request):
    posts = Post.objects.filter(date_pub__lte=timezone.now()).order_by('date_pub')
    return render(request, 'posts/post_list.html', {'posts': posts})



@login_required
def post_new(request):
=======
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
>>>>>>> parent of 70f5b37... conflicts resolved
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
<<<<<<< HEAD
        form = PostForm()
    return render(request, 'posts/post_edit.html', {'form': form,})


def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')



=======
        form = PostForm(instance=post)
    return render(request, 'posts/post_edit.html', {'form': form})
>>>>>>> 7fb98766f5dbb77e4003ff5f56b114ec32fa665a
>>>>>>> parent of 70f5b37... conflicts resolved
