"""
tests

:author: lishanZheng
:date: 2020/01/02
"""
from django.test import TestCase
from semester.models import Semester
from semester.test.generate.semester import get_semester_data
from util import result_util


class TestModifySemester(TestCase):
    """
    修改学期测试

    :author: lishanZheng
    :date: 2020/01/02
    """

    def setUp(self):
        self.semester_data = get_semester_data()
        semester_one = Semester(**self.semester_data)
        semester_one.save()
        self.semester = semester_one

    def test_modify_semester(self):
        """
        修改学期

        :author: lishanZheng
        :date: 2020/01/02
        """
        self.semester_data['period_semester'] = 3
        self.semester_data['subject'] = 'modify'
        res = self.client.put('/semester/semester/' + str(self.semester.id),
                              content_type="application/x-www-form-urlencoded",
                              data=self.semester_data)
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
        semester_get = res.get('data')
        self.assertIsNotNone(semester_get)
        self.assertEqual(semester_get.get('subject'), self.semester.subject)
        self.assertEqual(semester_get.get('period_semester'), self.semester.period_semester)
