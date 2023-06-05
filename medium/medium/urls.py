"""medium URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import BlogSitemap

sitemaps = {
    'posts': BlogSitemap,
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('blog.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("account/", include('account.urls', namespace='account')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
=======



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('blog.urls', namespace='blog')),
]
>>>>>>> 2ba3fbcf7569e8f3f5a154ce9d20e2a0d529993b

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)