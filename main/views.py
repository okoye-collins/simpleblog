from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

# Create your views here.

# def home(request):
#     return render(request, 'main/home.html')


class HomeView(ListView):
    model = Post
    template_name = 'main/home.html'
    ordering = ['-id'] 


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'main/article_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "main/add_post.html"

class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "main/update_post.html"
    # fields = ['title', 'tag', 'body']


class DeletePostView(DeleteView):
    model=Post
    template_name = "main/delete_post.html"
    success_url = reverse_lazy('home')