from django.conf.urls import url
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/new/', views.post_new, name='post_new'),
    re_path('post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path('post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    re_path('post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
]
