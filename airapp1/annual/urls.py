from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'annual'

urlpatterns = [
    url(r'^$', views.homeview.as_view(), name='index'),
    url(r'^(?P<url>\w+)/$', views.detail, name='site'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
