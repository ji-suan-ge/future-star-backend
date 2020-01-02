"""
tests

:author: lishanZheng
:date: 2020/01/02
"""
from django.test import TestCase

from util import result_util


class TestSemesterAdd(TestCase):
    """
    添加学期测试

    :author: lishanZheng
    :date: 2020/01/02
    """

    semester_data = {'period_semester': 1,
                     'subject': '测试主题',
                     'introduction': '测试介绍'}

    def test_add_semester(self):
        """
        添加学期

        :author: lishanZheng
        :date: 2020/01/02
        """
        res = self.client.post('/semester/semester',
                               data=self.semester_data)
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
        semester = res.get('data')
        self.assertIsNotNone(semester)
        self.assertEqual(semester.get('subject'), '测试主题')
        self.assertEqual(semester.get('introduction'), '测试介绍')
