"""
activity urls

:author: gexuewen
:date: 2020/01/01
"""
from django.urls import path

from activity import views

LIST_ACTIVITY = 'list_activity'

urlpatterns = [
    path(LIST_ACTIVITY, views.ActivityList.as_view()),
]
