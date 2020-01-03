"""
student list tests

:author: lishanZheng
:date: 2020/01/03
"""
from django.test import TestCase
from clazz.models import Clazz, ClazzStudent
from semester.models import Semester
from semester.test.generate.generate import get_semester_data
from student.generate.application import get_application_data
from student.generate.company import get_company_data
from student.generate.evaluation import get_evaluation_data
from student.generate.student import get_student_data
from student.models import Company, Student, Evaluation, ApplicationInformation
from util import result_util


class TestStudentList(TestCase):
    """
    获取校友列表单元测试

    :author: lishanZheng
    :date: 2020/01/03
    """
    student_data = get_student_data()
    student = ''
    company_data = get_company_data()
    evaluation_data = get_evaluation_data()
    semester_data = get_semester_data()
    semester = ''
    application_data = get_application_data()
    clazz_data = {
        'name': '班级名字',
        'introduction': '班级介绍',
        'start_time': '2020-01-02',
        'end_time': '2020-01-03',
        'people_number_limit': 1000,
        'current_people_number': 100,
        'state': 2,
    }
    clazz_student = ''

    def setUp(self):
        application = ApplicationInformation(**self.application_data)
        application.save()
        company = Company(**self.company_data)
        company.save()
        student = Student(company_id=company.id, **self.student_data)
        student.save()
        self.student = student
        evaluation = Evaluation(**self.evaluation_data)
        evaluation.save()
        semester = Semester(**self.semester_data)
        semester.save()
        self.semester = semester
        clazz = Clazz(**self.clazz_data, semester_id=semester.id)
        clazz.save()
        clazz_student = ClazzStudent(state=2,
                                     apply_id=application.id,
                                     clazz_id=clazz.id,
                                     evaluation_id=evaluation.id,
                                     student_id=student.id)
        clazz_student.save()
        self.clazz_student = clazz_student

    def test_student_list(self):
        """
        分页获取校友信息

        :author: lishanZheng
        :date: 2020/01/03
        """
        company = Company(**self.company_data)
        company.save()
        student = Student(company_id=company.id, **self.student_data)
        student.save()
        res = self.client.get('/student/student',
                              data={
                                  'page_size': 1,
                                  'page': 2
                              })
        result = res.json()
        results = result.get('data')
        self.assertEqual(result['code'], result_util.SUCCESS)
        self.assertEqual(results.get('results')[0].get('name'), student.name)

    def test_student_list_by_semester(self):
        """
        按学期获取校友信息

        :author: lishanZheng
        :date: 2020/01/03
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
        按课程获取校友信息

        :author: lishanZheng
        :date: 2020/01/03
        """
        res = self.client.get('/student/student',
                              data={
                                  'page_size': 1,
                                  'page': 1,
                                  'clazz_id': self.clazz_student.clazz_id,
                              })
        result = res.json()
        results = result.get('data')
        self.assertEqual(results.get('results')[0].get('name'), self.student.name)
        self.assertEqual(result['code'], result_util.SUCCESS)

    def test_student_list_by_name(self):
        """
        按姓名获取校友信息

        :author: lishanZheng
        :date: 2020/01/03
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
