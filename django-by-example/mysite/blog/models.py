from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Custom Manager
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')
        # .all() will return the custom queryset: Post.objects.filter(status='published')
        # Post.published.filter(title__startswith='Who') will return all published posts whose title starts with 'Who'


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
                    #choices parameter means the value of status field can only be set to one of the given choices.
    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager (see below)


    class Meta:
        ordering = ('-publish',)  #the negative prefix tells Django to sort results in descending order

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year, self.publish.strftime('%m'),
                                                            self.publish.strftime('%d'), self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments') # related name allows us to retrieve all comments of a post
      # using post.comments.all(). If this isnt defined Django would use commnent_set as default name
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)  #allows manual deactivation of inappropriate comments

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)




