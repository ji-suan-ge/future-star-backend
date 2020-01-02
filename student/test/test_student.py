"""
tests

:author: lishanZheng
:date: 2019/12/28
"""
from django.test import TestCase

from clazz.models import ClazzStudent, Clazz
from semester.models import Semester
from student.models import Company, Student, Evaluation, ApplicationInformation
from util import result_util


class StudentTest(TestCase):
    """
    学生模块单元测试

    :author: lishanZheng
    :date: 2020/01/01
    """
    student_data = {
        'name': '郑小鸽',
        'gender': 0,
        'birthday': '2020-01-01',
        'phone_number': '15256530000',
        'wx': '6028',
        'email': '60@qq.com',
        'city': '福建',
        'education': 'PhD',
        'school': 'HFU',
        'previous_company': '阿里',
        'previous_position': 'CWO',
        'state': 2}
    student_id = 1
    company_data = {
        'name': '郑公司',
        'website': 'zheng.com',
        'wx_public': 'zheng',
        'create_time': '2020-01-01',
        'city': '福建',
        'number_employee': 1000,
        'position': 'CTO',
        'introduction': '我是郑总的公司',
        'company_data': '10E',
        'income_scale': '收入1E',
        'financing_situation': 'others',
        'value_of_assessment': '100E'
    }

    evaluation_data = {
        'fraction': 0,
        'description': '未评价'
    }

    application_data = {
        'accept_absence': 0,
        'reason_application': '申请理由',
        'contribution_for_us': '我的贡献',
        'way': 'wx'
    }

    clazz_data = {
        'name': '班级名字',
        'introduction': '班级介绍',
        'start_time': '2020-01-02',
        'end_time': '2020-01-03',
        'people_number_limit': 1000,
        'current_people_number': 100,
        'state': 2,
    }
    clazz_id = 1
    semester_data = {
        'period_semester': 1,
        'subject': '主题',
        'introduction': '介绍',
        'state': 1
    }
    semester_id = 1

    def setUp(self):
        company = Company(**self.company_data)
        company.save()
        student = Student(company_id=company.id, **self.student_data)
        student.save()
        self.student_id = student.id
        evaluation = Evaluation(**self.evaluation_data)
        evaluation.save()
        application = ApplicationInformation(**self.application_data)
        application.save()
        semester = Semester(**self.semester_data)
        semester.save()
        self.semester_id = semester.id
        clazz = Clazz(**self.clazz_data, semester_id=semester.id)
        clazz.save()
        self.clazz_id = clazz.id
        clazz_student = ClazzStudent(state=1,
                                     apply_id=application.id,
                                     clazz_id=clazz.id,
                                     evaluation_id=evaluation.id,
                                     student_id=student.id)
        clazz_student.save()

    def test_student_list(self):
        """
        分页获取校友信息

        :author: lishanZheng
        :date: 2020/01/01
        """
        res = self.client.get('/student/student',
                              data={
                                  'page_size': 2,
                                  'page': 1
                              })
        result = res.json()
        self.assertEqual(result['code'], result_util.SUCCESS)

    def test_student_list_by_semester_or_clazz(self):
        """
        按学期或者课程获取校友信息

        :author: lishanZheng
        :date: 2020/01/02
        """
        res = self.client.get('/student/student',
                              data={
                                  'page_size': 2,
                                  'page': 1,
                                  'semester_id': self.semester_id,
                                  'clazz_id': self.clazz_id
                              })
        result = res.json()
        results = result.get('data')
        self.assertEqual(len(results.get('results')), 1)
        self.assertEqual(results.get('results')[0].get('name'), '郑小鸽')
        self.assertEqual(result['code'], result_util.SUCCESS)

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
