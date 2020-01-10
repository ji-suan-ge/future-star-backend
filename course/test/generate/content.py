"""
generate content

:author: lishanZheng
:date: 2020/01/03
"""

from django.utils.crypto import get_random_string

from course.models import Content
from course.test.generate.course import get_course


def get_content_data():
    """
    生成一个课程条目数据

    :author: lishanZheng
    :date: 2020/01/03
    """
    content_data = {'content_name': 'content_name_' + get_random_string(),
                    'sort': 'url'}
    return content_data


def get_content():
    """
    生成一个课程条目

    :author: lishanZheng
    :date: 2020/01/03
    """
    content_data = get_content_data()
    content = Content(**content_data, course=get_course())
    content.save()
    return content


def get_section():
    """
    生成条目返回模版

    :author: lishanZheng
    :date: 2020/01/09
    """
    return {'content': {}}
