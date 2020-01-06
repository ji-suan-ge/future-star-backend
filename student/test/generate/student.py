"""
student data generator

:author: gexuewen
:date: 2020/01/02
"""

import random

from django.utils.crypto import get_random_string

from student.models import Student
from student.test.generate.company import get_company


def get_student_data():
    """
    generate student data

    :author: gexuewen
    :date: 2020/01/02

    :modify by lishanZheng
    :data: 2020/01/06
    """
    month = random.randint(10, 12)
    day = random.randint(10, 20)
    student_data = {
        'name': 'name_' + get_random_string(),
        'gender': random.randint(0, 1),
        'birthday': '1998-%s-%s' % (month, day),
        'phone_number': '1525653' + str(random.randint(1000, 9999)),
        'wx': 'wx' + get_random_string(),
        'email': str(random.randint(1000, 9999)) + '@qq.com',
        'city': 'city_' + get_random_string(),
        'education': 'education' + get_random_string(),
        'school': 'school' + get_random_string(),
        'previous_company': 'previous_company' + get_random_string(),
        'previous_position': 'previous_position' + get_random_string(),
        'state': random.randint(1, 2),
    }
    return student_data


def get_student():
    """
    生成一个校友

    :author: lishanZheng
    :date: 2020/01/06
    """
    company = get_company()
    student_data = get_student_data()
    student = Student.objects.create(**student_data, company=company)
    return student
