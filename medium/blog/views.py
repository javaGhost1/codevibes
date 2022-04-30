from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Blog

# Create your views here.
class BlogListView(ListView):
    queryset = Blog.published.all()
    context_object_name = 'blogs'
    template_name = 'blog/list.html'

