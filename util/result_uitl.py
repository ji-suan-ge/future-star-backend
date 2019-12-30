"""
result util

:author: lishanZheng
:date: 2019/12/30
"""
from django.http import JsonResponse


def success(data):
    """
    success

    :author: lishanZheng
    :date: 2019/12/30
    """
    return JsonResponse({
        'code': "2000",
        'msg': '请求成功',
        'data': data
    })


def error(error_code, message):
    """
    error

    :author: lishanZheng
    :date: 2019/12/30
    """
    return JsonResponse({
        'code': error_code,
        'msg': message
    })
