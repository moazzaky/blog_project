from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post



# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username = 'testuser',
            email = 'test@yahoo.com',
            password = 'secret',
        )

        self.post = Post.objects.create(title='test title pk',
                                        body='text body',
                                        user=self.user)

    def test_string_repr(self):
        post = Post(title='test title')
        self.assertEqual(str(post),'test title')

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','test title pk')
        self.assertEqual(f'{self.post.body}', 'text body')
        self.assertEqual(f'{self.post.user}', 'testuser')

    def test_post_list_view(self):
        response = self.client.get(reverse('home_url'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'blog/home.html')
        self.assertContains(response,'test title pk')

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/1000/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)

        self.assertTemplateUsed(response,'blog/post_detail.html' and 'base.html')  #LOL
        self.assertContains(response,'test title pk')

