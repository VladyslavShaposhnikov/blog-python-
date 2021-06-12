from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.http import HttpResponseRedirect 
from django.urls import reverse_lazy, reverse

def LikeView(request, slug):
    post = get_object_or_404(Post, slug=request.POST.get('post_slug'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(slug)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-published_on']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats).order_by('-published_on')
    return render(request, 'categories.html', {'cats':cats, 'category_posts':category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all().order_by('name')
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all().order_by('name')
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, slug=self.kwargs['slug'])
        total_likes = stuff.total_likes()
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

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