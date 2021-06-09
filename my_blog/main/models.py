from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):

    STATUS = {
        (0,'Draft'),
        (1,'Publish')
    }

    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    published_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.slug])

