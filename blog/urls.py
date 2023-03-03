from django.urls import path
from . import views
from .feeds import LatestPostsFeed
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('tag/<slug:tag_slug>/', views.blog_list, name='blog_list_by_tag'),
    # path("", views.BlogListView.as_view(), name='blog_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:blog>/', views.blog_detail, name='blog_detail'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)