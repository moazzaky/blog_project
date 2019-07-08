from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post



# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        #Create a user
        self.user = get_user_model().objects.create(
            username = 'testuser',
            email = 'test@yahoo.com',
            password = 'secret',
        )
        #Create a Post
        self.post = Post.objects.create(title='test title pk',
                                        body='text body',
                                        user=self.user)

    def test_string_repr(self):
        # post = Post(title='test title')
        self.assertEqual(self.post.__str__(),'test title pk')

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

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

    def test_post_create_view(self):
        respone = self.client.post('/post/new/',
                                   {'title':'New title',
                                    'user': self.user,
                                    'body': 'New Text'})
        self.assertEqual(respone.status_code,200)
        self.assertContains(respone,'New title')
        self.assertContains(respone, 'New Text')
        self.assertTemplateUsed(respone,'blog/create_post.html')



    def test_post_update_view(self):
        respone = self.client.post(reverse('edit_post_url', args='1'),
                                   {'title': 'updated title',
                                    'body': 'updated body'})
        self.assertEqual(respone.status_code, 302)
        # self.assertContains(respone, 'updated title')
        # self.assertContains(respone, 'updated body')

    def test_post_delete_view(self):
        response = self.client.post(reverse('delete_post_url', args='1'))
        self.assertEqual(response.status_code,302)