from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from taggit.managers import TaggableManager
# Create your models here.
class Menu(models.Model):
    """links, images, videos"""
    image = models.ImageField(upload_to='images/')
    links = models.URLField()
    video = EmbedVideoField()
    
    def __str__(self) -> str:
        return self.image
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Blog(models.Model):
    """represent blog fields"""
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150)
    featured_image = models.ImageField(upload_to='images/', blank=True)
    body = models.TextField()
    # menu = models.ForeignKey(Menu, null=True, choices=MENU_CHOICES, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    favourites = models.ManyToManyField(User, related_name='favourite_blogs', blank=True)
    # default manager
    objects = models.Manager
    # custom manager
    published = PublishedManager()
    tags = TaggableManager()
    def get_absolute_url(self):
        return reverse("blog:blog_detail", args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
    

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    """Creating a comment system"""
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
