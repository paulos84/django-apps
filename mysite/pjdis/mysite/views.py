from django.shortcuts import render
from django.views import generic
from .models import Project, Post, Tag


class Index(generic.ListView):
    model = Project
    context_object_name = 'project'
    template_name = 'index.html'

class PostListView(generic.ListView):
    model = Post
    context_object_name = 'post'

class PostDetailView(generic.DetailView):
    model = Post
