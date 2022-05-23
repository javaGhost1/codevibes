from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Blog

# Create your views here.
class BlogListView(ListView):
    queryset = Blog.published.all()
    context_object_name = 'blogs'
    template_name = 'blog/list.html'

def blog_detail(request, year, month, day, blog):
    blog = get_object_or_404(Blog, slug=blog, status='published', publish__year=year, publish__month=month, publish__day=day)
    context = {'blog': blog}
    return render(request, 'blog/details.html', context)