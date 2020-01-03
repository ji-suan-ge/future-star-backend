"""
semester list test

:author: lishanZheng
:date: 2020/01/02
"""
from django.test import TestCase

import util.result_util as result_util
from semester.models import Semester
from semester.test.generate.generate import get_semester_data


class TestSemesterList(TestCase):
    """
    分页获取学期测试

    :author: lishanZheng
    :date: 2020/01/03
    """

    semesters_data = []

    def setUp(self):
        self.semesters_data.append(get_semester_data())
        self.semesters_data.append(get_semester_data())
        for semester_data in self.semesters_data:
            semester = Semester(**semester_data)
            semester.save()

    def test_semester_list(self):
        """
        分页获取学期

        :author: lishanZheng
        :date: 2020/01/03
        """
        res = self.client.get('/semester/semester',
                              data={
                                  'page': 2,
                                  'page_size': 1
                              })
        result = res.json()
        data = result.get('data')
        self.assertEqual(result.get('code'), result_util.SUCCESS)
        self.assertIsNotNone(data)
        results = data.get('results')
        self.assertEqual(len(results), 1)
        semester = results[0]
        self.assertEqual(self.semesters_data[1].get('name'), semester.get('name'))
