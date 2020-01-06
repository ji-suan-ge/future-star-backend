"""
company data generator

:author: gexuewen
:date: 2020/01/02
"""
import random

from django.utils.crypto import get_random_string


def get_company_data():
    """
    generate company data

    :author: gexuewen
    :date: 2020/01/02

    :modify by lishanZheng
    :data: 2020/01/06
    """
    month = random.randint(10, 12)
    day = random.randint(10, 20)
    company_data = {
        'name': 'name_' + get_random_string(),
        'website': get_random_string() + '.com',
        'wx_public': 'wx_public_' + get_random_string(),
        'create_time': '1998-%s-%s' % (month, day),
        'city': 'city_' + get_random_string(),
        'number_employee': random.randint(500, 1000),
        'position': 'position_' + get_random_string(),
        'introduction': 'introduction_' + get_random_string(),
        'company_data': 'company_data_' + get_random_string(),
        'income_scale': 'income_scale_' + get_random_string(),
        'financing_situation': 'financing_' + get_random_string(),
        'value_of_assessment': 'value_' + get_random_string(),
    }
    return company_data
