from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-post/', AddPostView.as_view(), name='add-post'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('edit/<slug:slug>/', UpdatePostView.as_view(), name='update-post'),
    path('remove/<slug:slug>/', DeletePostView.as_view(), name='delete-post'),
    path('category-list/', CategoryListView, name='category-list'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('like/<slug:slug>/', LikeView, name='like-post'),
]