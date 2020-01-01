"""
urls

:author: lishanZheng
:date: 2019/12/28
"""
from django.conf.urls import url
from administrator import views

urlpatterns = [
    url('login', views.login, name='login'),
    url('logout', views.logout, name='logout'),
    url('add', views.add, name='add'),
    url('modify_pri', views.modify_privilege, name='modify_privilege'),
]
