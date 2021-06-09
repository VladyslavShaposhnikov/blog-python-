from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    queryset = Post.objects.order_by('-published_on')

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = 'title', 'body', 'author', 'slug'