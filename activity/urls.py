"""
activity urls

:author: gexuewen
:date: 2020/01/01
"""
from django.urls import path
from activity.views import activity as activity_view
from activity.views import student as student_view

urlpatterns = [
    path('activity', activity_view.ActivityViewSet.as_view()),
    path('activity/<int:primary_key>', activity_view.ActivityDetailViewSet.as_view()),
    path('student', student_view.StudentActivityViewSet.as_view())
]
