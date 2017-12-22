"""app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from annual import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sites/', include('annual.urls')),

    url(r'^api/annual-means/$', views.annual_means.as_view(), name='annual_means'),
    url(r'^api/annual-means/sites/(?P<url>\w+)/$', views.site_annual_means.as_view()),
    url(r'^api/annual-means/pollutants/(?P<poll>\w+)/$', views.pollutant_annual_means.as_view()),

    url(r'^api/daily-means/$', views.daily_means.as_view(), name='daily_means'),
    url(r'^api/daily-means/sites/(?P<url>\w+)/$', views.site_daily_means.as_view()),
    url(r'^api/daily-means/pollutants/(?P<poll>\w+)/$', views.pollutant_daily_means.as_view()),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#if settings.DEBUG:
 #   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  #  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #for when in development mode and image files stored on local comp not on server
    #when in development need to change DEBUG=TRUE to DEBUG=FALSE in settings...see 33 Introduction to Django Tutorial Uploading Files

