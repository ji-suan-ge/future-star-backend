"""
add activity test

:author: gexuewen
:date: 2020/01/02
"""
from django.test import TestCase

import util.result_util as result_util
from activity.test.generate.activity import get_activity_data


class TestActivityAdd(TestCase):
    """
    添加活动测试

    :author: gexuewen
    :date: 2020/01/02
    """

    def setUp(self):
        self.activity_data = get_activity_data()

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
        self.assertEqual(activity.get('name'), self.activity_data.get('name'))
        self.assertEqual(activity.get('price'), self.activity_data.get('price'))
