from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('edit/<slug:slug>/', UpdatePostView.as_view(), name='update-post'),
    path('remove/<slug:slug>/', DeletePostView.as_view(), name='delete-post'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]