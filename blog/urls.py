from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'blog'
urlpatterns = [
    path("", views.BlogListView.as_view(), name='blog_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:blog>/', views.blog_detail, name='blog_detail'),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)