from django.conf.urls import url
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    re_path('post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
