"""
activity student add test

:author: gexuewen
:date: 2020/01/03
"""
from activity.constant.activity_student_state import WAIT_FOR_PAY
from activity.constant.code import ALREADY_JOIN
from activity.test.base_test.activity_student import ActivityStudentBaseTest
from util import result_util


class TestActivityStudentJoin(ActivityStudentBaseTest):
    """
    校友加入活动测试

    :author: gexuewen
    :date: 2020/01/02
    """
    def setUp(self):
        super(TestActivityStudentJoin, self).setUp()
        self.activity_to_join = self.activities[0]
        self.student_for_join = self.students[0]

    def test_activity_student_join(self):
        """
        加入活动

        :author: gexuewen
        :date: 2020/01/03
        """
        res = self.send()
        result = res.json()
        self.assertEqual(result.get('code'), result_util.SUCCESS)
        data = result.get('data')
        self.assertIsNotNone(data)
        state = data.get('state')
        self.assertEqual(state, WAIT_FOR_PAY)
        res = self.send()
        result = res.json()
        self.assertEqual(result.get('code'), ALREADY_JOIN)

    def send(self):
        return self.client.post('/activity/student',
                                data={
                                    'activity_id': self.activity_to_join.id,
                                    'student_id': self.student_for_join.id
                                })
