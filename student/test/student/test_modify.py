"""
student tests

:author: lishanZheng
:date: 2020/01/03
"""
from django.test import TestCase

from student.models import Student
from student.test.generate.student import get_student
from util import result_util


class TestModifyStudent(TestCase):
    """
    修改学生信息测试

    :author: lishanZheng
    :date: 2020/01/06
    """

    def setUp(self):
        student = get_student()
        self.student_id = student.id

    def test_modify_student(self):
        """
        修改学生信息

        :author: lishanZheng
        :date: 2020/01/06
        """
        res = self.client.put('/student/student/' + str(self.student_id),
                              data={'name': 'XXX',
                                    'company': {
                                        'name': 'XX'
                                    }},
                              content_type="application/json")
        result = res.json()
        self.assertEqual(result['code'], result_util.SUCCESS)
        student = Student.objects.get(id=self.student_id)
        self.assertEqual(student.name, 'XXX')
        company = student.company
        self.assertEqual(company.name, 'XX')
