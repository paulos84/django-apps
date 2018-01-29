from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_example.urls'))
    #gives urls that can use for a user management system
    path('accounts/'), include('django.contrib.auth.urls')
]
