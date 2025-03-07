from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import BlogApp


class BlogListview(ListView):
    model = BlogApp
    template_name = "djblog/dj_blog_model.html"
class BlogDetailView(DetailView):
    model = BlogApp
    template_name = "djblog/blog_detail.html"
# Create your views here.
