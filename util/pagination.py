"""
pagination

:author: gexuewen
:date: 2020/01/01
"""
from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    """
    custom page number pagination

    :author: gexuewen
    :date: 2020/01/01
    """
    page_size = 1
    page_size_query_param = 'page_size'
