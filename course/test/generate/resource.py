"""
generate resource

:author: lishanZheng
:date: 2020/01/03
"""
import random

from django.utils.crypto import get_random_string

from course.models import Resource
from course.test.generate.content import get_content


def get_resource_data():
    """
    生成一个课程资源数据

    :author: lishanZheng
    :date: 2020/01/03
    """
    resource_data = {'name': 'name_' + get_random_string(),
                     'type': random.randint(0, 2),
                     'url': 'url_' + get_random_string(),
                     'word': 'word_' + get_random_string(),
                     'state': random.randint(0, 1),
                     }
    return resource_data


def get_resource():
    """
    生成一个课程资源

    :author: lishanZheng
    :date: 2020/01/03
    """
    resource = Resource(**get_resource_data(), content=get_content())
    resource.save()
    return resource
