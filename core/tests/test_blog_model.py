from django.test import TestCase
from blog.models import Post, Category
from datetime import datetime
from django.contrib.auth import get_user_model
from accounts.models import Profile
User = get_user_model()

class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='test@example.com', password='testtesttest')
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'testname',
            last_name = 'testlastname',
            description = 'test description',

        )

    def test_create_post_with_valid_data(self):
        
        category = Category.objects.create(name = "category")
        post = Post.objects.create(
            author = self.profile,
            title = "test",
            content = "description",
            status = True,
            category = category,
            publish_date = datetime.now() 
        )
        self.assertEqual(Post.objects.filter(pk=post.id).exists(), True)