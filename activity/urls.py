"""
activity urls

:author: gexuewen
:date: 2020/01/01
"""
from django.urls import path

from activity import views

LIST_ACTIVITY = 'list'
ADD_ACTIVITY = 'add'
# DELETE_ACTIVITY = ''

urlpatterns = [
    path(LIST_ACTIVITY, views.ActivityList.as_view()),
    path(ADD_ACTIVITY, views.AddActivity.as_view()),
    # path('delete/<int:id>', views.DeleteActivity.as_view())
]
