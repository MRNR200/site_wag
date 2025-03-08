from django.shortcuts import render
from django.views.generic import ListView , DetailView , CreateView , UpdateView
from .models import BlogApp


class BlogListview(ListView):
    model = BlogApp
    template_name = "djblog/dj_blog_model.html"
class BlogDetailView(DetailView):
    model = BlogApp
    template_name = "djblog/blog_detail.html"
class BlogCreateView(CreateView):
    model = BlogApp
    template_name = "djblog/blog_create.html"
    # fields = ['title' , 'content']
    fields = ['title']

class BlogUpdateView(UpdateView):
    model = BlogApp
    template_name = "djblog/blog_update.html"
    # fields = ['title' , 'content']
    fields = ['title']