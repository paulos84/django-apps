from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import RedirectView, TemplateView
from django.conf import settings
from django.conf.urls.static import static
import mysite.views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^$', RedirectView.as_view(url='/projects/', permanent=True)),
    re_path(r'^projects/$', mysite.views.Index.as_view(), name='index'),
    re_path(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    re_path(r'^blog/', include('mysite.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )