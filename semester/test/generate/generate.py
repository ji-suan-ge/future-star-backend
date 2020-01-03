"""
generate

:author: lishanZheng
:date: 2020/01/03
"""
import random

from django.utils.crypto import get_random_string


def get_semester_data():
    """
    生成一个学期

    :author: lishanZheng
    :date: 2020/01/03
    """
    semester_data = {'period_semester': random.randint(1, 10),
                     'subject': 'subject_' + get_random_string(),
                     'introduction': 'introduction_' + get_random_string()}
    return semester_data
