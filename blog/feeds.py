from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from django.template.defaultfilters import truncatewords
from .models import Blog

class LatestPostsFeed(Feed):
    title = 'My blog'
    link = reverse_lazy('blog:blog_list')
    description = 'Latest Posts'

    def items(self):
        return Blog.published.all()

    def item_title(self, item) -> str:
        return item.title
    def item_description(self, item):
        return truncatewords(item.body, 30)