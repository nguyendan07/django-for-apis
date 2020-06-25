from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post


class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user_1 = User.objects.create_user(username='user_1', password='12345678')
        user_1.save()

        post_1 = Post.objects.create(author=user_1, title="Blog title", body="Body content...")
        post_1.save()
        return super().setUpTestData()
    
    def test_blog_content(self):
        post = Post.objects.get(id=1)
        self.assertEqual(f'{post.author}', 'user_1')
        self.assertEqual(f'{post.title}', 'Blog title')
        self.assertEqual(f'{post.body}', 'Body content...')

