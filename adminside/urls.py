from django.urls import path
from . views import *

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("categories/", CategoriesView.as_view(), name="category-list"),
    path('categories/<int:pk>/', CategoryDetailAPIView.as_view(), name='category-detail'),
    path('items/', ItemsView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetailAPIView.as_view(), name='item-detail')
]