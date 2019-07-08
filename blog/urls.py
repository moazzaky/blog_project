from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home_url'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='detail_url'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new_url'),
    path('post/<int:pk>/update/', views.BlogUpdateView.as_view(), name='edit_post_url'),
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='delete_post_url')
]