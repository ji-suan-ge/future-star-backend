"""
activity student list test

:author: gexuewen
:date: 2020/01/02
"""
from django.test import TestCase

from activity.models import Activity
from activity.test.generate.activity import get_activity_data
from student.generate.company import get_company_data
from student.generate.student import get_student_data
from student.models import Student, Company


class ActivityStudentBaseTest(TestCase):
    """
    分页获取活动校友测试

    :author: gexuewen
    :date: 2020/01/02
    """
    def __init__(self, method_name):
        super(ActivityStudentBaseTest, self).__init__(method_name)
        self.activities_data = []
        self.activities = []
        self.students_data = []
        self.students = []

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
