from django.views.generic import ListView, DetailView
from blog.models import Post


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 2
    ordering = "id"


class PostDetailView(DetailView):
    model = Post
