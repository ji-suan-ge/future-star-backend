"""
content

:author: lishanZheng
:date: 2020/01/04
"""
from django.test import TestCase

from course.test.generate.content import get_content_data
from course.test.generate.course import get_course
from util import result_util


class TestContent(TestCase):
    """
    条目测试

    :author: lishanZheng
    :date: 2020/01/04
    """

    def test_add_content(self):
        """
        添加目录

        :author: lishanZheng
        :date: 2020/01/04
        """
        content_data = get_content_data()
        course = get_course()
        content_data['course'] = course.id
        res = self.client.post('/course/content', data=content_data)
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
        content = res.get('data')
        self.assertIsNotNone(content)
        self.assertEqual(content.get('content_name'), content_data.get('content_name'))
