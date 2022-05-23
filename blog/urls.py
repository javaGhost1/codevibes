from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path("", views.BlogListView.as_view(), name='blog_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:blog>/', views.blog_detail, name='blog_detail'),
    
]
