"""akankshaarya URL Configuration
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from dataPeace import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/users', views.StudentList.as_view()),
    url(r'^api/users/(?P<id>[0-9]+)', views.StudentList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
