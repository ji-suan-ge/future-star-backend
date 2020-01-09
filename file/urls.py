"""
urls

:author: lishanZheng
:date: 2020/01/09
"""
from django.urls import path
from file.views import file

urlpatterns = [
    path('upload', file.upload),
]
