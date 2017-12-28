from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    re_path(r'^catalog/', include('catalog.urls')),
]

urlpatterns += [
    re_path(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# Use static() to add url mapping to serve static files during development (only)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)