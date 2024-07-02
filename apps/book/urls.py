from django.urls import path
from .views import BookListCreateView, BookDetailView, FavoriteListView, FavoriteCreateView , SoftDeleteBookView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('favorites/', FavoriteListView.as_view(), name='favorite-list'),
    path('favorites/add/', FavoriteCreateView.as_view(), name='favorite-add'),
    path('books/<int:pk>/soft-delete/', SoftDeleteBookView.as_view(), name='book-soft-delete'),
]
