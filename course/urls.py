"""
urls

:author: lishanZheng
:date: 2020/01/03
"""
from django.urls import path

from course.views import resource, teacher

urlpatterns = [
    path('resource', resource.ResourceViewSet.as_view()),
    path('teacher', teacher.TeacherViewSet.as_view())
]
