from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Profile(models.Model):

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images/profile")
    website_url = models.CharField(max_length=255,null=True, blank=True)
    fb_url = models.CharField(max_length=255,null=True, blank=True)
    twitter_url = models.CharField(max_length=255,null=True, blank=True)
    instagram_url = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return str(self.user)

class Post(models.Model):

    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    body = RichTextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.CharField(max_length=255, default='Coding')
    snippet = models.CharField(max_length=255, default='Click Link Above To Read Blog Post')
    likes = models.ManyToManyField(User, related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article-detail', args=[self.slug])

