"""Crescent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from base.views.views import *
from base.views.auth import *
from django.urls import path
from Crescent import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = []

blog_url = [
    
    path('list_edit_blog',list_edit_blog),
    path('view_blog/<str:pk>',view_blog),
    path('edit_blog/<str:pk>',edit_blog),
    path('blog_edit',blog_edit),
    path('save_blog',save_blog),
    path('delete_blog',delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>',save_edit_blog),
    path('', home),
    path('home', home, name="home"),
    
    path('new_page',new_page),
    path('list_blog',list_blog),
    path('blogs',blogs),
    path('list_edit_blog',list_edit_blog),
    path('view_blog/<str:pk>',view_blog),
    path('edit_blog/<str:pk>',edit_blog),
    path('blog_edit',blog_edit),
    path('save_blog',save_blog),
    path('delete_blog',delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>',save_edit_blog),
    
    
]

auth = [
    path('accounts/', include('django.contrib.auth.urls')),  # Use built-in authentication views
    path('enter_otp', enter_otp, name='enter_otp'),
    path('signup/<str:mail>', signup, name='signup'),
    path('login', user_login, name='login'),
    
    path('save_blog1/<str:post_id>', save_blog1, name='save_blog1'),
    
    path('comments/<str:id>', comments, name='comments'),
    path('create_comment/<str:path>' , create_comment , name='create_comment'),
    
]

urlpatterns.extend(blog_url)
urlpatterns.extend(auth)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
