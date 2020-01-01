"""
activity urls

:author: gexuewen
:date: 2020/01/01
"""
from django.urls import path

from activity import views

urlpatterns = [
    path('list_activity', views.ActivityList.as_view()),
]
