from django.shortcuts import render

def post_list(request):
    return render(request, 'post/post_list.html', {})
