"""
clazz urls

:author: gexuewen
:date: 2020/01/04
"""
from django.urls import path

from clazz import views

urlpatterns = [
    path('clazz', views.ClazzViewSet.as_view()),
    path('clazz/<int:primary_key>', views.ClazzDetailViewSet.as_view())
]
