from django.test import TestCase,Client
from django.shortcuts import get_object_or_404
from django.urls import reverse
from blog.models import Category,Post,Comment
from datetime import datetime
class TestBlogViews(TestCase):

    def setUp(self):
        self.client=Client()
        self.blog_index=reverse('blog_index')
        self.blog_detail=reverse('blog_detail',args=[1])
        self.category1=Category.objects.create(
                name='programming'
                )
        self.blog_category=reverse('blog_category',args=[self.category1])
            
    def test_blog_index_GET(self):
        response=self.client.get(self.blog_index)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog_index.html')


    def test_blog_category_GET(self):
        response=self.client.get(self.blog_category)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'blog_category.html')


    def test_blog_detail_POST(self):
        self.category1= Category.objects.create(
               name='development'
               )
        self.post1=Post.objects.create(
                title='title',
                body="body",
                created_on=datetime.now(),
                last_modified=datetime.now(),
               
                )
        self.post1.categories.set([self.category1])

        
        response=self.client.post(self.blog_detail,{
            'author':'author',
            'body':'body',
            'post':self.post1
            })
        self.assertEquals(response.status_code,302)

    def test_blog_detail_POST_with_no_data(self):
        self.assertEquals(Post.objects.count(),0)

    

