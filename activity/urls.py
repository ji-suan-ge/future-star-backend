"""
activity urls

:author: gexuewen
:date: 2020/01/01
"""
from django.urls import path

from activity.view import activity as activity_view
from activity.view import clazz as clazz_view
from activity.view import student as student_view

urlpatterns = [
    path('activity', activity_view.ActivityViewSet.as_view()),
    path('activity/<int:primary_key>', activity_view.ActivityDetailViewSet.as_view()),
    path('student', student_view.ActivityStudentViewSet.as_view()),
    path('student/<int:activity_id>/<param>', student_view.ActivityStudentDetailViewSet.as_view()),
    path('clazz', clazz_view.ActivityClazzViewSet.as_view()),
    path('clazz/<int:activity_id>/<param>', clazz_view.ActivityClazzDetailViewSet.as_view())
]
