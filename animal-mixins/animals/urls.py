
from django.contrib import admin
from django.urls import path, re_path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^pets/$', views.PetListView.as_view(), name='pet_list'),
    re_path(r'^pets/(?P<pk>\d+)$', views.PetDetailView.as_view(), name='pet_detail'),
]
