"""
delete student test

:author: lishanZheng
:date: 2020/01/06
"""
from django.test import TestCase

from student.constant.student_state import INVALID
from student.models import Student
from student.test.generate.student import get_student
from util import result_util


class TestDeleteStudent(TestCase):
    """
    删除指定校友测试

    :author: lishanZheng
    :date: 2020/01/06
    """

    def setUp(self):
        student = get_student()
        self.student = student

    def test_delete_student(self):
        """
        删除指定校友

        :author: lishanZheng
        :date: 2020/01/06
        """
        res = self.client.delete('/student/student/' + str(self.student.id))
        result = res.json()
        self.assertEqual(result['code'], result_util.SUCCESS)
        student = Student.objects.get(id=self.student.id)
        self.assertEqual(student.state, INVALID)
