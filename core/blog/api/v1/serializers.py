from rest_framework import serializers
from blog.models import Post
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'category', 'status', 'created_date', 'publish_date', )