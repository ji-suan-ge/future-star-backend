"""
generate administrator

:author: lishanZheng
:date: 2020/01/06
"""
import random

from django.utils.crypto import get_random_string

from administrator.models import Administrator
from util.encrypt import encrypt


def get_administrator_data():
    """
    生成管理员数据

    :author: lishanZheng
    :date: 2020/01/06
    """
    administrator_data = {
        'account': 'account' + get_random_string(),
        'password': encrypt('123'),
        'name': 'name_' + get_random_string(),
        'state': random.randint(0, 1),
    }
    return administrator_data


def get_administrator():
    """
    生成管理员

    :author: lishanZheng
    :date: 2020/01/06
    """
    administrator_data = get_administrator_data()
    administrator = Administrator.objects.create(**administrator_data)
    return administrator
