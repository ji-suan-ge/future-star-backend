"""
activity student list test

:author: gexuewen
:date: 2020/01/02
"""
from activity.constant.activity_student_state import WAIT_FOR_PAY
from activity.models import ActivityStudent
from activity.test.activity_student.activity_student import ActivityStudentBaseTest
from util import result_util


class TestActivityStudentList(ActivityStudentBaseTest):
    """
    分页获取活动校友测试

    :author: gexuewen
    :date: 2020/01/02
    """

    def setUp(self):
        super(TestActivityStudentList, self).setUp()
        self.activity_to_add = None
        self.activity_students = []
        self.activity_to_add = self.activities[0]
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
        result = self.client.get('/activity/student',
                                 data={
                                     'page': 3,
                                     'page_size': 2,
                                     'activity_id': self.activity_to_add.id
                                 }).json()
        self.assertEqual(result.get('code'), result_util.SUCCESS)
        data = result.get('data')
        results = data.get('results')
        student = self.students[5]
        result_student = results[1]
        self.assertEqual(result_student.get('name'), student.name)
