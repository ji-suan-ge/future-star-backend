"""
tests

:author: lishanZheng
:date: 2020/01/02
"""
from django.test import TestCase

from semester.models import Semester
from semester.test.generate.generate import get_semester_data
from util import result_util


class TestSemesterAdd(TestCase):
    """
    添加学期测试

    :author: lishanZheng
    :date: 2020/01/02
    """

    def test_add_semester(self):
        """
        添加学期

        :author: lishanZheng
        :date: 2020/01/02
        """
        semester_data = get_semester_data()
        semester = Semester(**semester_data)
        res = self.client.post('/semester/semester',
                               data=semester_data)
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
        semester_get = res.get('data')
        self.assertIsNotNone(semester_get)
        self.assertEqual(semester_get.get('subject'), semester.subject)
        self.assertEqual(semester_get.get('introduction'), semester.introduction)
