from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home_url'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='detail_url')
]