"""
generate privilege

:author: lishanZheng
:date: 2020/01/06
"""
import random

from administrator.models import Privilege


def get_privilege_data():
    """
    生成权限数据

    :author: lishanZheng
    :date: 2020/01/06
    """
    privilege_data = {
        'enrollment': random.randint(1, 2),
        'semester': random.randint(1, 2),
        'activity': random.randint(1, 2),
        'student': random.randint(1, 2)
    }
    return privilege_data


def get_privilege():
    """
    生成权限

    :author: lishanZheng
    :date: 2020/01/06
    """
    privilege_data = get_privilege_data()
    privilege = Privilege.objects.create(**privilege_data)
    return privilege
