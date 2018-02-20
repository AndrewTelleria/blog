from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path

from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', views.login, name='login'),
    path('accounts/logout/', views.logout, name='logout', kwargs={'next_page':'/'}),
    path('', include('posts.urls')),
]
