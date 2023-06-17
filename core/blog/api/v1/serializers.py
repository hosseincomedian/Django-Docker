from rest_framework import serializers
from blog.models import Post, Category, Category

class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source = 'get_snippet')
    relative_path = serializers.URLField(source = 'get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'snippet', 'category', 'status', 'relative_path', 'absolute_url', 'created_date', 'publish_date', )

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.pk)   

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')