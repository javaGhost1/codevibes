from django.urls import path
from . import views
<<<<<<< HEAD
from .feeds import LatestPostsFeed
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('tag/<slug:tag_slug>/', views.blog_list, name='blog_list_by_tag'),
    # path("", views.BlogListView.as_view(), name='blog_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:blog>/', views.blog_detail, name='blog_detail'),
    path('search/', views.post_search, name='post_search'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======

app_name = 'blog'
urlpatterns = [
    path("", views.BlogListView.as_view(), name='blog_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:blog>/', views.blog_detail, name='blog_detail'),
    
]
>>>>>>> 2ba3fbcf7569e8f3f5a154ce9d20e2a0d529993b
