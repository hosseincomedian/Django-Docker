from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime
from accounts.models import Profile
from blog.models import Post, Category

User = get_user_model()
class TestBlogView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='test@example.com', password='testtesttest')
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'testname',
            last_name = 'testlastname',
            description = 'test description',

        )
        self.category = Category.objects.create(name = "category")
        self.post = Post.objects.create(
            author = self.profile,
            title = "test",
            content = "description",
            status = True,
            category = self.category,
            publish_date = datetime.now() 
        )


    def test_blog_post_detail_is_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse('blog:post-detail', kwargs={'pk': self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_post_detail_anonymous_response(self):
        url = reverse('blog:post-detail', kwargs={'pk': self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

 
    # def test_url_without_data_200(self):
    #     url = reverse('index')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200) 
    #     self.assertTrue(str(response.content).find('index'))
    #     self.assertTemplateUsed(response, 'index.html')