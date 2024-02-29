from django.shortcuts import render 
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

# def home(request):
#     return render(request, 'main/home.html')


class HomeView(ListView):
    model = Post
    template_name = 'main/home.html'


class ArticleDetailView(DetailView):
    model=Post
    template_name='main/article_detail.html'