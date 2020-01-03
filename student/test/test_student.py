"""
student tests

:author: lishanZheng
:date: 2020/01/03
"""
from django.test import TestCase

from student.generate.company import get_company_data
from student.generate.student import get_student_data
from student.models import Company, Student
from util import result_util


class StudentTest(TestCase):
    """
    学生列表模块单元测试

    :author: lishanZheng
    :date: 2020/01/01
    """
    student_data = get_student_data()
    company_data = get_company_data()
    student_id = 1

    def setUp(self):
        company = Company(**self.company_data)
        company.save()
        student = Student(company_id=company.id, **self.student_data)
        student.save()
        self.student_id = student.id

    def test_delete_student(self):
        """
        删除指定校友

        :author: lishanZheng
        :date: 2020/01/02
        """
        res = self.client.delete('/student/student/' + str(self.student_id))
        result = res.json()
        self.assertEqual(result['code'], result_util.SUCCESS)
        student = Student.objects.get(id=self.student_id)
        self.assertEqual(student.state, 0)

    def test_modify_student(self):
        """
        修改校友信息

        :author: lishanZheng
        :date: 2020/01/02
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
