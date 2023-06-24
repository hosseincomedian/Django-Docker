from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import PostListView, PostDetailView

class TestUrl(TestCase):

    def test_post_url_resolve(self):
        url = reverse('blog:post-list')
        self.assertEqual(resolve(url).func.view_class, PostListView)

    def test_post_detail_url_resolve(self):
        url = reverse('blog:post-detail', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, PostDetailView)
