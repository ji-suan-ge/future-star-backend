"""
activity list test

:author: gexuewen
:date: 2020/01/01
"""
from django.test import TestCase

from activity.models import Activity
import util.result_util as result_util


class TestActivityList(TestCase):
    """
    分页获取活动测试

    :author: gexuewen
    :date: 2020/01/01
    """

    activities_data = [
        {
            'name': 'test activity  1',
            'enroll_start_time': '2020-01-01',
            'enroll_end_time': '2020-01-02',
            'organizer': 'he',
            'start_time': '2020-01-05',
            'address': 'an hui',
            'arrangement': 'Day1: nothing',
            'price': 100,
            'people_number_limit': 50,
            'current_people_number': 10
        }, {
            'name': 'test activity 2',
            'enroll_start_time': '2020-01-02',
            'enroll_end_time': '2020-01-03',
            'organizer': 'he',
            'start_time': '2020-01-05',
            'address': 'an hui',
            'arrangement': 'Day1: nothing',
            'price': 100,
            'people_number_limit': 50,
            'current_people_number': 10
        }, {
            'name': 'test activity 3',
            'enroll_start_time': '2020-01-02',
            'enroll_end_time': '2020-01-03',
            'organizer': 'he',
            'start_time': '2020-01-05',
            'address': 'an hui',
            'arrangement': 'Day1: nothing',
            'price': 100,
            'people_number_limit': 50,
            'current_people_number': 10
        }
    ]

    def setUp(self):
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
                                  'page_size': 2
                              })
        result = res.json()
        self.assertEqual(result.get('code'), result_util.SUCCESS)
        data = result.get('data')
        self.assertIsNotNone(data)
        results = data.get('results')
        self.assertEqual(len(results), 1)
        activity = results[0]
        self.assertEqual('test activity 3', activity.get('name'))
