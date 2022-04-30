from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from embed_video.fields import EmbedVideoField

# Create your models here.
# class Menu(models.Model):
#     """links, images, videos"""
#     image = models.ImageField(upload_to='images/')
#     links = models.URLField()
#     video = EmbedVideoField()
    
#     def __str__(self) -> str:
#         return self.image
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
    # default manager
    objects = models.Manager
    # custom manager
    published = PublishedManager()

    def __str__(self) -> str:
        return self.title

