"""
add activity test

:author: gexuewen
:date: 2020/01/02
"""
from django.test import TestCase

import util.result_util as result_util


class TestActivityAdd(TestCase):
    """
    添加活动测试

    :author: gexuewen
    :date: 2020/01/02
    """

    activity_data = {
        'name': 'activity 1',
        'enroll_start_time': '2020-12-01',
        'enroll_end_time': '2020-12-02',
        'organizer': 'heh',
        'start_time': '2020-12-05',
        'address': 'an hui he fei',
        'arrangement': 'Day2: nothing',
        'price': 200,
        'people_number_limit': 60,
        'current_people_number': 20}

    def test_add_activity(self):
        """
        添加活动

        :author: gexuewen
        :date: 2020/01/02
        """
        res = self.client.post('/activity/activity',
                               data=self.activity_data)
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
        activity = res.get('data')
        self.assertIsNotNone(activity)
        self.assertEqual(activity.get('name'), 'activity 1')
        self.assertEqual(activity.get('price'), 200)
