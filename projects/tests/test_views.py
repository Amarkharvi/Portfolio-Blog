from django.test import TestCase,Client
from django.urls import reverse
from projects.models import Project

class TestViews(TestCase):

    def setUp(self):
        self.client=Client()
        self.list_url=reverse('project_index')
        first_project_detail_primarykey=1
        self.list_detail=reverse('project_detail',args=[first_project_detail_primarykey])

    def test_project_list_GET(self):
        response=self.client.get(self.list_url)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'project_index.html')

