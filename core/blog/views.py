from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from blog.models import Post

def indexview(request):
    return render(request, 'index.html')



    
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 2 
    ordering = 'id'

class PostDetailView(DetailView):
    model = Post