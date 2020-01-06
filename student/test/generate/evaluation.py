"""
evaluation data generator

:author: gexuewen
:date: 2020/01/02
"""
import random

from django.utils.crypto import get_random_string


def get_evaluation_data():
    """
    generate evaluation data

    :author: gexuewen
    :date: 2020/01/02

    :modify by lishanZheng
    :data: 2020/01/06
    """
    evaluation_data = {
        'fraction': random.randint(0, 1),
        'description': 'description_' + get_random_string(),
    }
    return evaluation_data
