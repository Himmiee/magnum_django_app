from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'

urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('v', views.about_page, name='about_page'),
    path('v1', views.contact_page, name='contact_page'),
    path('v2', views.home_page, name='home_page'),
    path('v6', views.blog_page, name='blog_page'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    # path('', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/',views.post_list, name='post_list_by_tag'),
   
]