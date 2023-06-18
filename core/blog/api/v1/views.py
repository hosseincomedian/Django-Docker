from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from blog.models import Post, Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .permissions import PostAuthorPermission
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .pagination import DefaultPagination

class PostModelViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticatedOrReadOnly, PostAuthorPermission)
        queryset = Post.objects.filter(status=True)
        serializer_class = PostSerializer   
        filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
        filterset_fields = ('author', 'category', 'status',)
        search_fields = ['title', 'content']
        ordering_fields = ('publish_date',)
        pagination_class = DefaultPagination
        
        
class CategoryModelViewSet(viewsets.ModelViewSet):
        permission_classes = (IsAuthenticatedOrReadOnly,)
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
