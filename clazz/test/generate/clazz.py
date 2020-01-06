"""
clazz generator

:author: gexuewen
:date: 2020/01/03
"""
from django.utils.crypto import get_random_string

from clazz.constant.clazz_state import UNOPENED
from clazz.models import Clazz
from semester.models import Semester
from semester.test.generate.semester import get_semester_data


def get_clazz_data():
    """
    generate clazz data

    :author: gexuewen
    :date: 2020/01/03
    """
    clazz_data = {
        'name': 'clazz_' + get_random_string(),
        'introduction': 'clazz introduction',
        'start_time': '2020-06-02',
        'end_time': '2020-08-03',
        'people_number_limit': 100,
        'current_people_number': 10,
        'state': UNOPENED,
    }
    return clazz_data


def get_clazz():
    """
    生成一个课程

    :author: lishanZheng
    :date: 2020/01/03
    """
    semester_data = get_semester_data()
    semester = Semester(**semester_data)
    semester.save()
    clazz_data = get_clazz_data()
    clazz = Clazz(**clazz_data, semester=semester)
    clazz.save()
    return clazz
