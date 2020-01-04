"""
content modify

:author: lishanZheng
:date: 2020/01/04
"""
from django.test import TestCase

from course.test.generate.content import get_content_data, get_content
from util import result_util


class TestModifyContent(TestCase):
    """
    修改条目测试

    :author: lishanZheng
    :date: 2020/01/04
    """

    def test_modify_content(self):
        """
        修改条目

        :author: lishanZheng
        :date: 2020/01/04
        """
        content = get_content()
        content_data = get_content_data()
        res = self.client.put('/course/content/' + str(content.id),
                              data=content_data,
                              content_type='application/json')
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
        data = res.get('data')
        self.assertEqual(data.get('content_name'), content_data.get('content_name'))
