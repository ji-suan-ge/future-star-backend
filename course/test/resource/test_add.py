"""
add resource test

:author: lishanZheng
:date: 2019/12/28
"""
from django.test import TestCase

from course.test.generate.content import get_content
from course.test.generate.resource import get_resource_data
from util import result_util


class TestAddResource(TestCase):
    """
    添加课程资源测试

    :author: lishanZheng
    :date: 2020/01/03
    """

    def test_add_resource(self):
        """
        添加资源

        :author: lishanZheng
        :date: 2020/01/03
        """
        resource_data = get_resource_data()
        content = get_content()
        resource_data['content'] = content.id
        res = self.client.post('/course/resource', data=resource_data)
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
        resource = res.get('data')
        self.assertIsNotNone(resource)
        self.assertEqual(resource.get('name'), resource_data.get('name'))
        self.assertEqual(resource.get('url'), resource_data.get('url'))
