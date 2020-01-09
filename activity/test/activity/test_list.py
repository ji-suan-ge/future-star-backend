"""
activity list test

:author: gexuewen
:date: 2020/01/01
"""
from django.test import TestCase

import util.result_util as result_util
from activity.constant import activity_state
from activity.models import Activity
from activity.test.generate.activity import get_activity_data


class TestActivityList(TestCase):
    """
    分页获取活动测试

    :author: gexuewen
    :date: 2020/01/01
    """

    def setUp(self):
        self.activities_data = []
        for i in range(0, 3):
            if i == -1:
                pass
            self.activities_data.append(get_activity_data())
        for activity_data in self.activities_data:
            activity = Activity(**activity_data)
            activity.save()

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
                                  'activity_state': activity_state.PUBLISHED
                              })
        result = res.json()
        self.assertEqual(result.get('code'), result_util.SUCCESS)
        data = result.get('data')
        self.assertIsNotNone(data)
        results = data.get('results')
        self.assertEqual(len(results), 1)
        activity = results[0]
        self.assertEqual(self.activities_data[2].get('name'), activity.get('name'))
