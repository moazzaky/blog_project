from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog\post_detail.html'
    pk_url_kwarg = 'pk'                        # you can change this to whatever u like.

    # context_object_name =                     ...........Name of ur choice



