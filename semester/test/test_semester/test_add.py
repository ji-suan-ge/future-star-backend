"""
tests

:author: lishanZheng
:date: 2020/01/02
"""
from django.test import TestCase
from semester.test.generate.semester import get_semester_data
from util import result_util


class TestAddSemester(TestCase):
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
        result = self.client.post('/semester/semester',
                                  data=semester_data)
        result = result.json()
        self.assertEqual(result.get('code'), result_util.SUCCESS)
        semester_get = result.get('data')
        self.assertIsNotNone(semester_get)
        self.assertEqual(semester_get.get('introduction'), semester_data.get('introduction'))
        self.assertEqual(semester_get.get('subject'), semester_data.get('subject'))
