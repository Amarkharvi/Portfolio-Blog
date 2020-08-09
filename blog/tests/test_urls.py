from django.test import SimpleTestCase
from django.urls import reverse,resolve
from blog.views import blog_index,blog_category,blog_detail

class TestBlogUrls(SimpleTestCase):
    def test_blog_index_is_resolved(self):
        url=reverse('blog_index')
        self.assertEquals(resolve(url).func,blog_index)


    def test_blog_detail_is_resolved(self):
        url=reverse('blog_detail',args=['pname'])
        self.assertEquals(resolve(url).func,blog_detail)

#TODO resolve category path
    """def test_blog_category_is_resolved(self):
        url=reverse('blog_category',args=['category'])
        self.assertEquals(resolve(url).func,blog_category)"""
