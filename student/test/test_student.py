"""
tests

:author: lishanZheng
:date: 2019/12/28
"""
from django.test import TestCase
from student.models import Company, Student
from util import result_util


class StudentTest(TestCase):
    """
    学生模块单元测试

    :author: lishanZheng
    :date: 2020/01/01
    """
    student_data = [{
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
        'state': 2}]

    company_data = [{
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
    }]

    def setUp(self):
        for company_data in self.company_data:
            company = Company(name=company_data['name'],
                              website=company_data['website'],
                              wx_public=company_data['wx_public'],
                              create_time=company_data['create_time'],
                              city=company_data['city'],
                              number_employee=company_data['number_employee'],
                              position=company_data['position'],
                              introduction=company_data['introduction'],
                              company_data=company_data['company_data'],
                              income_scale=company_data['income_scale'],
                              financing_situation=company_data['financing_situation'],
                              value_of_assessment=company_data['value_of_assessment'])
            company.save()

        for student_data in self.student_data:
            student = Student(name=student_data['name'],
                              gender=student_data['gender'],
                              birthday=student_data['birthday'],
                              phone_number=student_data['phone_number'],
                              wx=student_data['wx'],
                              email=student_data['email'],
                              city=student_data['city'],
                              education=student_data['education'],
                              school=student_data['school'],
                              previous_company=student_data['previous_company'],
                              previous_position=student_data['previous_position'],
                              state=student_data['state'],
                              company_id=company.id)
            student.save()

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
