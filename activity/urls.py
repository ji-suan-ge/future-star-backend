"""
activity urls

:author: gexuewen
:date: 2020/01/01
"""
from django.urls import path
from activity import views

urlpatterns = [
    path('activity', views.ActivityViewSet.as_view()),
    # path('delete/<int:id>', views.DeleteActivity.as_view())
]
