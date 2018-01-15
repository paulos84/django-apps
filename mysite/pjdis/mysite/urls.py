from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.PostListView.as_view(), name='post_list'),
    re_path(r'^post/(?P<pk>\d+)$', views.PostDetailView.as_view(), name='post_detail'),
]

