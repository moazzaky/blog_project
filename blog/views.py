from django.shortcuts import render, Http404, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog\post_detail.html'
    pk_url_kwarg = 'pk'                        # you can change this to whatever u like.

    # context_object_name =                     ...........Name of ur choice


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    fields = ['title', 'body', 'tags']



# def BlogDeleteView(request, pk):
#     if request.method == 'POST':
#         post = get_object_or_404(Post,pk=pk)
#
#         post.delete()
#
#         return redirect('home_url')
#
#     else:
#
#         post = get_object_or_404(Post, pk = pk)
#         return render(request,'blog/delete_post.html',{'post':post})





class BlogDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home_url')
    template_name = 'blog/delete_post.html'











