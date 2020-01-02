"""
activity student list test

:author: gexuewen
:date: 2020/01/02
"""
from django.test import TestCase

from activity.constant.activity_student_state import WAIT_FOR_PAY
from activity.models import Activity, ActivityStudent
from activity.test.generate.activity import get_activity_data
from student.generate.company import get_company_data
from student.generate.student import get_student_data
from student.models import Student, Company
from util import result_util


class TestActivityStudentList(TestCase):
    """
    分页获取活动校友测试

    :author: gexuewen
    :date: 2020/01/02
    """

    activities_data = []
    activities = []
    students_data = []
    students = []
    activity_to_add = None
    activity_students = []

    def setUp(self):
        # 生成三个活动
        for i in range(0, 3):
            activity_data = get_activity_data()
            activity = Activity(**activity_data)
            activity.save()
            self.activities_data.append(activity_data)
            self.activities.append(activity)
        # 生成8个学生
        company_data = get_company_data()
        company = Company(**company_data)
        company.save()
        for i in range(0, 8):
            # make pylint happy
            if i == -1:
                pass
            student_data = get_student_data()
            student = Student(company=company, **student_data)
            student.save()
            self.students_data.append(student_data)
            self.students.append(student)
        self.activity_to_add = self.activities[1]
        # 将前6个学生加入第2个活动中
        for student in self.students:
            activity_student_data = {
                'activity': self.activity_to_add,
                'student': student,
                'state': WAIT_FOR_PAY
            }
            activity_student = ActivityStudent(**activity_student_data)
            activity_student.save()
            self.activity_students.append(activity_student)

    def test_activity_student_list(self):
        """
        分页获取活动校友

        :author: gexuewen
        :date: 2020/01/02
        """
        res = self.client.get('/activity/student',
                              data={
                                  'page': 3,
                                  'page_size': 2,
                                  'activity_id': self.activity_to_add.id
                              })
        result = res.json()
        self.assertEqual(result.get('code'), result_util.SUCCESS)
        data = result.get('data')

        self.assertIsNotNone(data)
        results = data.get('results')
        self.assertEqual(len(results), 2)
        activity_student = results[1]
        student = self.students[5]
        result_student = activity_student.get('student')
        self.assertEqual(result_student.get('name'), student.name)
