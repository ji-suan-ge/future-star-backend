"""
generate teacher

:author: lishanZheng
:date: 2020/01/03
"""
from django.utils.crypto import get_random_string

from course.models import Teacher


def get_teacher_data():
    """
    生成一个老师数据

    :author: lishanZheng
    :date: 2020/01/03
    """
    teacher_data = {'name': 'name_' + get_random_string(),
                    'avatar': 'avatar_' + get_random_string(),
                    'title': 'title_' + get_random_string(),
                    'introduction': 'introduction_' + get_random_string(),
                    'contact_way': 'way_' + get_random_string(),
                    }
    return teacher_data


def get_teacher():
    """
    生成一个老师

    :author: lishanZheng
    :date: 2020/01/03
    """
    teacher = Teacher(**get_teacher_data())
    teacher.save()
    return teacher
