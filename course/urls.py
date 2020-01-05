"""
urls

:author: lishanZheng
:date: 2020/01/03
"""
from django.urls import path

from course.views import resource, teacher, content, course

urlpatterns = [
    path('resource', resource.ResourceViewSet.as_view()),
    path('resource/<int:primary_key>', resource.ResourceDetailViewSet.as_view()),
    path('teacher', teacher.TeacherViewSet.as_view()),
    path('content', content.ContentViewSet.as_view()),
    path('content/<int:primary_key>', content.ContentDetailViewSet.as_view()),
    path('course', course.CourseViewSet.as_view()),
]
