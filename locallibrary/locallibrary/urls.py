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

# Use static() to add url mapping to serve static files during development only
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    re_path(r'^accounts/', include('django.contrib.auth.urls')),
]
"""
Using the above method adds the following urls with names in square brackets, used to reverse the url mappings.
^accounts/login/$ [name='login']
^accounts/logout/$ [name='logout']
^accounts/password_change/$ [name='password_change']
^accounts/password_change/done/$ [name='password_change_done']
^accounts/password_reset/$ [name='password_reset']
^accounts/password_reset/done/$ [name='password_reset_done']
^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^accounts/reset/done/$ [name='password_reset_complete']
^accounts/login/$ [name='login']
^accounts/logout/$ [name='logout']
^accounts/password_change/$ [name='password_change']
^accounts/password_change/done/$ [name='password_change_done']
^accounts/password_reset/$ [name='password_reset']
^accounts/password_reset/done/$ [name='password_reset_done']
^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^accounts/reset/done/$ [name='password_reset_complete']
"""