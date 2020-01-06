"""
evaluation data generator

:author: gexuewen
:date: 2020/01/02
"""
import random

from django.utils.crypto import get_random_string

from student.models import Evaluation


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


def get_evaluation():
    """
    生成一个评价

    :author: lishanZheng
    :date: 2020/01/06
    """
    evaluation_data = get_evaluation_data()
    evaluation = Evaluation.objects.create(**evaluation_data)
    return evaluation
