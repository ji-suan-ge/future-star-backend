"""
activity list test

:author: gexuewen
:date: 2020/01/01
"""
from django.test import TestCase

import util.result_util as result_util
from activity.constant import activity_state
from activity.models import Activity, ActivityStudent
from activity.test.generate.activity import get_activity_data
from student.test.generate.student import get_student


class TestActivityList(TestCase):
    """
    分页获取活动测试

    :author: gexuewen
    :date: 2020/01/01
    """

    def setUp(self):
        self.activities = []
        for i in range(0, 3):
            if i == -1:
                pass
            activity_data = get_activity_data()
            activity_data['state'] = activity_state.ENROLLING
            activity = Activity.objects.create(**activity_data)
            self.activities.append(activity)
        self.student = get_student()
        self.another_student = get_student()
        for activity in self.activities:
            ActivityStudent.objects.create(activity=activity, student=self.student)
            ActivityStudent.objects.create(activity=activity, student=self.another_student)
        # 添加一个额外的学生和活动
        activity_data = get_activity_data()
        activity = Activity.objects.create(**activity_data)
        ActivityStudent.objects.create(activity=activity, student=self.another_student)

    def test_activity_list(self):
        """
        分页获取活动

        :author: gexuewen
        :date: 2020/01/01
        """
        res = self.client.get('/activity/activity',
                              data={
                                  'page': 2,
                                  'page_size': 2,
                                  'activity_state': activity_state.ENROLLING,
                                  'student_id': self.student.id
                              })
        result = res.json()
        self.assertEqual(result.get('code'), result_util.SUCCESS)
        data = result.get('data')
        self.assertIsNotNone(data)
        results = data.get('results')
        self.assertEqual(len(results), 1)
        activity = results[0]
        self.assertEqual(self.activities[2].name, activity.get('name'))
