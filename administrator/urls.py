"""
urls

:author: lishanZheng
:date: 2019/12/28
"""
from django.urls import path

from administrator import views

urlpatterns = [
    path('login', views.login),
    path('logout', views.logout),
    path('administrator', views.AdministratorList.as_view()),
    path('delete', views.delete),
    path('modify', views.modify)
]
