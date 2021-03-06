from audioop import reverse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from .models import Post


# Create your views here.
class PostListView(generic.ListView):
  model = Post
  fields = '__all__'
  success_url = reverse_lazy('blog:all')

class PostCreateView(generic.CreateView):
  model = Post
  fields = '__all__'
  success_url: reverse_lazy('blog:all')

class PostDetailView(generic.DetailView):
  mpdel = Post

class PostUpdateView(generic.UpdateView):
  model = Post
  fields = '__all__'
  success_url: reverse_lazy('blog:all')

class PostDeleteView(generic.DeleteView):
  model = Post
  fields = '__all__'
  success_url: reverse_lazy('blog:all')