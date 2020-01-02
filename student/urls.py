"""
urls

:author: lishanZheng
:date: 2020/01/01
"""
from django.urls import path

from student import views

urlpatterns = [
    # path('login', views.login),
    path('student', views.StudentList.as_view()),
    path('student/<int:primary_key>', views.StudentDetailViewSet.as_view())
]
