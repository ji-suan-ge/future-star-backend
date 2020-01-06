"""
generate administrator

:author: lishanZheng
:date: 2020/01/06
"""

from django.utils.crypto import get_random_string

from administrator.models import Administrator
from administrator.test.generate.privilege import get_privilege
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
        'state': 1,
    }
    return administrator_data


def get_administrator():
    """
    生成管理员  密码为123

    :author: lishanZheng
    :date: 2020/01/06
    """
    administrator_data = get_administrator_data()
    privilege = get_privilege()
    administrator = Administrator.objects.create(**administrator_data,
                                                 privilege=privilege)
    return administrator
