from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from annual import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
