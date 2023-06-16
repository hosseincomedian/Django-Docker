from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView


class PostList(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer

    def get(self, request):
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PostDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = PostSerializer
    
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True)
        post.delete()
        return Response({"message": "Item removed successfully"}, status=status.HTTP_204_NO_CONTENT)


