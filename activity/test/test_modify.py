"""
modify activity test

:author: gexuewen
:date: 2020/01/02
"""
from django.test import TestCase

import util.result_util as result_util
from activity.models import Activity


class TestActivityAdd(TestCase):
    """
    修改活动测试

    :author: gexuewen
    :date: 2020/01/02
    """

    activity_data = {
        'name': 'before modify',
        'enroll_start_time': '2020-10-01',
        'enroll_end_time': '2020-10-02',
        'organizer': 'heh',
        'start_time': '2020-10-05',
        'address': 'an hui',
        'arrangement': 'Day3: nothing',
        'price': 200,
        'people_number_limit': 60,
        'current_people_number': 50
    }

    def setUp(self):
        activity_data = self.activity_data
        activity = Activity(**activity_data)
        activity.save()
        self.activity = activity

    def test_add_activity(self):
        """
        修改活动

        :author: gexuewen
        :date: 2020/01/02
        """
        self.activity_data['name'] = 'modify name'
        self.activity_data['price'] = 300
        res = self.client.put('/activity/activity/' + str(self.activity.id),
                              data=self.activity_data,
                              content_type="application/x-www-form-urlencoded")
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)

        activity = res.get('data')
        self.assertIsNotNone(activity)

        self.assertNotEqual(activity.get('name'),
                            self.activity_data.get('name'))

        self.assertNotEqual(activity.get('price'),
                            self.activity_data.get('price'))

        self.assertEqual(activity.get('enroll_start_time'),
                         self.activity_data.get('enroll_start_time'))
