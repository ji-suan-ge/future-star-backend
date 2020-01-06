"""
application data generator

:author: gexuewen
:date: 2020/01/02
"""
import random

from django.utils.crypto import get_random_string


def get_application_data():
    """
    generate application data

    :author: gexuewen
    :date: 2020/01/02

    :modify by lishanZheng
    :data: 2020/01/06
    """
    application_data = {
        'accept_absence': random.randint(0, 1),
        'reason_application': 'application_' + get_random_string(),
        'contribution_for_us': 'contribution_' + get_random_string(),
        'way': 'wx'
    }
    return application_data
