"""
content

:author: lishanZheng
:date: 2020/01/04
"""
from django.test import TestCase

from course.models import Content
from course.test.generate.content import get_content
from util import result_util


class TestDeleteContent(TestCase):
    """
    删除条目测试

    :author: lishanZheng
    :date: 2020/01/04
    """

    def test_delete_content(self):
        """
        删除目录

        :author: lishanZheng
        :date: 2020/01/04
        """
        content = get_content()
        res = self.client.delete('/course/content/' + str(content.id))
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
        content = Content.objects.filter(id=content.id)
        self.assertEqual(0, len(content))
