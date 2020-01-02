"""
activity data generator

:author: gexuewen
:date: 2020/01/02
"""
import random

from django.utils.crypto import get_random_string


def get_activity_data():
    """
    generate activity data

    :author: gexuewen
    :date: 2020/01/02
    """
    month = random.randint(10, 12)
    day = random.randint(10, 20)
    activity_data = {
        'name': 'activity_' + get_random_string(),
        'enroll_start_time': '2020-%s-%s' % (month, day),
        'enroll_end_time': '2020-%s-%s' % (month, day + 1),
        'organizer': 'he',
        'start_time': '2020-%s-%s' % (month, day + 5),
        'address': 'an hui',
        'arrangement': 'Day1: nothing',
        'price': random.randint(100, 600),
        'people_number_limit': random.randint(200, 250),
        'current_people_number': random.randint(0, 50)
    }
    return activity_data
