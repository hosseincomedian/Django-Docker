from blog.models import Post, Category
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import DefaultPagination
from .serializers import PostSerializer, CategorySerializer
from .permissions import PostAuthorPermission


class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly, PostAuthorPermission)
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        "author": ["exact", "in"],
        "category": ["exact", "in"],
        "status": ["exact", "in"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ("publish_date",)
    pagination_class = DefaultPagination


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
