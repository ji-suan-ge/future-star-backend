"""
generate course

:author: lishanZheng
:date: 2020/01/03
"""
import random

from django.utils.crypto import get_random_string

from clazz.test.generate.clazz import get_clazz
from course.models import Course
from course.test.generate.teacher import get_teacher


def get_course_data():
    """
    生成一个课程数据

    :author: lishanZheng
    :date: 2020/01/03
    """
    course_data = {'name': 'name_' + get_random_string(),
                   'introduction': 'introduction_' + get_random_string(),
                   'location': 'location_' + get_random_string(),
                   'begin_time': '2020-06-02',
                   'end_time': '2020-07-02',
                   'sort': 'sort_' + get_random_string(),
                   'state': random.randint(0, 1),
                   }
    return course_data


def get_course():
    """
    生成一个课程

    :author: lishanZheng
    :date: 2020/01/03
    """
    clazz = get_clazz()
    teacher = get_teacher()
    course_data = get_course_data()
    course = Course(**course_data, clazz=clazz, teacher=teacher)
    course.save()
    return course
