from django.test import TestCase
from mysite.models import Post


class PostModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Post.objects.create(title='My First Post', content='The post content')

    def test_post_title_label(self):
        project=Post.objects.get(id=1)
        field_label = project._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'Post Title')

    def test_object_name_is_project_title(self):
        post = Post.objects.get(id=1)
        expected_object_name = post.title
        self.assertEquals(expected_object_name,str(post))

    def test_first_name_max_length(self):
        author=Post.objects.get(id=1)
        max_length = author._meta.get_field('title').max_length
        self.assertEquals(max_length,300)

    def test_get_absolute_url(self):
        project = Post.objects.get(id=1)
        self.assertEquals(project.get_absolute_url(),'/blog/post/1')
