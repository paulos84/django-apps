from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


BYADMIN_CHOICES = (
    (1, "Yes"),
    (0, "No"))


class Project(models.Model):
    title = models.CharField(max_length=300, verbose_name='Project Title', help_text="Enter the project title")
    description = models.TextField(max_length=1000, help_text="Enter a brief description")
    is_python = models.BooleanField(choices=BYADMIN_CHOICES,default=1)
    url = models.URLField(max_length=1000, help_text='URL link')
    github = models.URLField(blank=True, null=True, max_length=1000, help_text='GitHub link')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a tag (e.g. Flask-SQLAlchemy or pandas")

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=300, verbose_name='Post Title', help_text="Enter the post title")
    content = RichTextUploadingField()
    is_published = models.BooleanField(choices=BYADMIN_CHOICES, default=0)
    is_featured = models.BooleanField(choices=BYADMIN_CHOICES, default=0)
    created = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, help_text="Select a tag for this post")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


