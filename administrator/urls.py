"""
urls

:author: lishanZheng
:date: 2019/12/28
"""
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from administrator import views

ROUTER = routers.DefaultRouter()
urlpatterns = [
    path('', include(ROUTER.urls)),
    url(r'login', views.login, name='login'),
]
