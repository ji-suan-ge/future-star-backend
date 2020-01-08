"""
student list test

:author: lishanZheng
:date: 2020/01/03
"""
from django.test import TestCase

from clazz.models import Clazz, ClazzStudent
from clazz.test.generate.clazz import get_clazz_data
from semester.test.generate.semester import get_semester
from student.constant.student_state import VALID
from student.test.generate.application import get_application_information
from student.test.generate.evaluation import get_evaluation
from student.test.generate.student import get_student
from util import result_util


class TestStudentListBy(TestCase):
    """
    获取校友列表测试

    :author: lishanZheng
    :date: 2020/01/06
    """

    def setUp(self):
        semester = get_semester()
        evaluation = get_evaluation()
        student_one = get_student()
        application = get_application_information()
        clazz_data = get_clazz_data()
        clazz = Clazz.objects.create(**clazz_data, semester_id=semester.id)
        student_two = get_student()
        ClazzStudent.objects.create(state=VALID,
                                    student_id=student_one.id,
                                    apply_id=application.id,
                                    clazz_id=clazz.id,
                                    evaluation_id=evaluation.id)
        semester = get_semester()
        clazz = Clazz.objects.create(**clazz_data, semester_id=semester.id)
        clazz_student = ClazzStudent.objects.create(state=VALID,
                                                    apply_id=application.id,
                                                    clazz_id=clazz.id,
                                                    evaluation_id=evaluation.id,
                                                    student_id=student_two.id)
        self.student = student_two
        self.semester = semester
        self.clazz_student = clazz_student

    def test_student_list(self):
        """
        分页获取校友信息

        :author: lishanZheng
        :date: 2020/01/06
        """
        res = self.client.get('/student/student',
                              data={
                                  'page_size': 1,
                                  'page': 2
                              })
        result = res.json()
        data_student_list = result.get('data')
        results_student_list = data_student_list.get('results')
        self.assertEqual(result['code'], result_util.SUCCESS)
        student = results_student_list[0]
        self.assertEqual(student.get('name'), self.student.name)
        self.assertEqual(student.get('email'), self.student.email)
        self.assertEqual(student.get('wx'), self.student.wx)

    def test_student_list_by_semester(self):
        """
        按学期获取校友信息

        :author: lishanZheng
        :date: 2020/01/06
        """

        res = self.client.get('/student/student',
                              data={
                                  'page_size': 1,
                                  'page': 1,
                                  'semester_id': self.semester.id,
                              })
        result = res.json()
        results = result.get('data')
        self.assertEqual(results.get('results')[0].get('id'), self.student.id)
        self.assertEqual(result['code'], result_util.SUCCESS)

    def test_student_list_by_clazz(self):
        """
        按班级获取校友信息

        :author: lishanZheng
        :date: 2020/01/06
        """
        res = self.client.get('/student/student',
                              data={
                                  'page_size': 1,
                                  'page': 1,
                                  'clazz_id': self.clazz_student.clazz_id

                              })
        result = res.json()
        results = result.get('data')
        self.assertEqual(results.get('results')[0].get('name'), self.student.name)
        self.assertEqual(result['code'], result_util.SUCCESS)

    def test_student_list_by_name(self):
        """
        按姓名获取校友信息

        :author: lishanZheng
        :date: 2020/01/06
        """
        res = self.client.get('/student/student',
                              data={
                                  'page_size': 1,
                                  'page': 1,
                                  'name': self.student.name,
                              })
        result = res.json()
        results = result.get('data')
        self.assertEqual(results.get('results')[0].get('name'), self.student.name)
        self.assertEqual(result['code'], result_util.SUCCESS)

    def test_student_list_by_letter(self):
        """
        按字母顺序获取校友信息

        :author: lishanZheng
        :date: 2020/01/06
        """
        student = get_student()
        letter = 'A'
        student.name = letter
        student.save()
        res = self.client.get('/student/student/letter',
                              content_type="application/x-www-form-urlencoded")
        result = res.json()
        results = result.get('data')
        self.assertEqual(results.get('results')[0].get('letter'), letter)
        self.assertEqual(results.get('results')[0].get('group')[0]['name'], letter)
        self.assertEqual(result['code'], result_util.SUCCESS)
