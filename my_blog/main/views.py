from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect 
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-published_on']

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats).order_by('-published_on')
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'    

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')