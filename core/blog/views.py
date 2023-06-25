from django.views.generic import ListView, DetailView
from blog.models import Post
from django.contrib.auth.mixins import LoginRequiredMixin


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = "id"


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
