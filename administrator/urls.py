"""
urls

:author: lishanZheng
:date: 2019/12/28
"""
from django.urls import path

from administrator import views

LIST_ADMINISTRATOR = 'list_administrator'

urlpatterns = [
    path('login', views.login),
    path('logout', views.logout),
    path('add', views.add),
    path('modify_pri', views.modify_privilege),
    path('delete', views.delete),
]
