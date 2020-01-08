"""
clazz urls

:author: gexuewen
:date: 2020/01/04
"""
from django.urls import path

import clazz.view.clazz as clazz_view

urlpatterns = [
    path('clazz', clazz_view.ClazzViewSet.as_view()),
    path('clazz/<int:primary_key>', clazz_view.ClazzDetailViewSet.as_view())
]
