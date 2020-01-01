"""
result util

:author: lishanZheng
:date: 2019/12/30
"""
from django.http import JsonResponse

SUCCESS = '2000'


def success(data):
    """
    success

    :author: lishanZheng
    :date: 2019/12/30
    """
    return JsonResponse({
        'code': SUCCESS,
        'msg': '请求成功',
        'data': data
    })


def success_empty():
    """
    success

    :author: lishanZheng
    :date: 2019/12/30
    """
    return JsonResponse({
        'code': SUCCESS,
        'msg': '请求成功',
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
