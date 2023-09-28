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
<<<<<<< HEAD:blog/urls.py
    # new blog
    path('new_blog/', views.new_blog, name='new_blog'),
=======
>>>>>>> d32a961ec6d747a0d677f67036b53b44970dcf36:medium/blog/urls.py
    path('search/', views.post_search, name='post_search'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)