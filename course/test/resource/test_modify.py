"""
test modify

:author: lishanZheng
:date: 2020/01/04
"""
from django.test import TestCase

from course.test.generate.resource import get_resource_data, get_resource
from util import result_util


class TestModifyResource(TestCase):
    """
    修改课程资源测试

    :author: lishanZheng
    :date: 2020/01/04
    """

    def setUp(self):
        resource = get_resource()
        self.resource = resource

    def test_modify_resource(self):
        """
        修改资源

        :author: lishanZheng
        :date: 2020/01/04
        """
        resource_data = get_resource_data()
        res = self.client.put('/course/resource/' + str(self.resource.id),
                              data=resource_data,
                              content_type="application/json")
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
        resource = res.get('data')
        self.assertEqual(resource.get('name'), resource_data.get('name'))
        self.assertEqual(resource.get('word'), resource_data.get('word'))
        self.assertEqual(resource.get('state'), resource_data.get('state'))
        self.assertEqual(resource.get('url'), resource_data.get('url'))
        self.assertEqual(resource.get('type'), resource_data.get('type'))
