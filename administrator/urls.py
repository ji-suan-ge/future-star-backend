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
    path('administrator', views.AdministratorViewSet.as_view()),
    path('administrator/<int:primary_key>', views.AdministratorDetailViewSet.as_view()),
]
