from django.test import TestCase
from mysite.models import Project
from django.urls import reverse


class ProjectListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Project.objects.create(title='My First Project', description='The first proj')
        Project.objects.create(title='My Second Project', description='The second proj')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/projects/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_context_dict(self):
        proj_1 = Project.objects.get(pk=1)
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('project' in resp.context)
        self.assertEqual(proj_1.title, 'My First Project')
        self.assertEqual(proj_1.is_python, True)

