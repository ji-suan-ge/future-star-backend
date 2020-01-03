"""
generate clazz

:author: lishanZheng
:date: 2020/01/03
"""
import random

from django.utils.crypto import get_random_string

from clazz.models import Clazz
from semester.models import Semester
from semester.test.generate.semester import get_semester_data


def get_clazz_data():
    """
    生成一个课程条目数据

    :author: lishanZheng
    :date: 2020/01/03
    """
    month = random.randint(10, 12)
    day = random.randint(10, 20)
    clazz_data = {'name': 'name_' + get_random_string(),
                  'introduction': 'introduction_' + get_random_string(),
                  'start_time': '2020-%s-%s' % (month, day),
                  'end_time': '2020-%s-%s' % (month, day + 1),
                  'people_number_limit': random.randint(50, 100),
                  'current_people_number': random.randint(1, 40),
                  'state': random.randint(0, 2),
                  }
    return clazz_data


def get_clazz():
    """
    生成一个课程条目

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
