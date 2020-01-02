"""
student data generator

:author: gexuewen
:date: 2020/01/02
"""


import random

from django.utils.crypto import get_random_string


def get_student_data():
    """
    generate student data

    :author: gexuewen
    :date: 2020/01/02
    """
    month = random.randint(10, 12)
    day = random.randint(10, 20)
    student_data = {
        'name': 'name_' + get_random_string(),
        'gender': 0,
        'birthday': '1998-%s-%s' % (month, day),
        'phone_number': '15256530000',
        'wx': '6028',
        'email': '60@qq.com',
        'city': '福建',
        'education': 'PhD',
        'school': 'HFU',
        'previous_company': '阿里',
        'previous_position': 'CWO',
        'state': 2
    }
    return student_data
