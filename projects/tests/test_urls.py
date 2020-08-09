from django.test import SimpleTestCase
from django.urls import reverse,resolve
from projects.views import project_index,project_detail

class TestUrls(SimpleTestCase):

    def test_project_index_is_resolved(self):
        url=reverse('project_index')
        self.assertEquals(resolve(url).func,project_index)


    def test_project_detail_is_resolved(self):
        first_detail_page=1
        url=reverse('project_detail',args=[first_detail_page])
        self.assertEquals(resolve(url).func,project_detail)
