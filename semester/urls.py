"""
urls

:author: lishanZheng
:date: 2020/01/02
"""
from django.urls import path

from semester import views

urlpatterns = [
    path('semester', views.SemesterViewSet.as_view()),
    path('semester/<int:primary_key>', views.SemesterDetailViewSet.as_view())
]
