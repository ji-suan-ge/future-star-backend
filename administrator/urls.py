"""
urls

:author: lishanZheng
:date: 2019/12/28
"""
from django.conf.urls import url
from administrator import views

urlpatterns = [
    url(r'login', views.login, name='login'),
    url(r'logout', views.logout, name='logout'),
    url(r'add', views.add, name='add'),
]
