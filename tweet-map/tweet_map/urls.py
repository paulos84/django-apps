from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
import app.views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  re_path(r'^$', RedirectView.as_view(url='/tweets/', permanent=True)),
                  re_path(r'^tweets/$', app.views.TweetListView.as_view(), name='tweet_list'),
                  re_path(r'^map$', app.views.TweetMapView.as_view(), name='tweet_map'),
                  re_path(r'^countries/$', app.views.CountryListView.as_view(), name='countries'),
                  re_path(r'^countries/(?P<pk>\d+)$', app.views.CountryDetailView.as_view(), name='country_detail'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
