from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
]