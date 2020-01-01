"""
activity list test

:author: gexuewen
:date: 2020/01/01
"""
from django.test import TestCase

from activity.models import Activity
import activity.urls as activity_urls
import util.result_uitl as result_util
from config import urls
from util.url import get_url


class TestActivityList(TestCase):
    """
    活动测试

    :author: gexuewen
    :date: 2020/01/01
    """

    activities_data = [{
        'name': 'test activity  1',
        'enroll_start_time': '2020-01-01',
        'enroll_end_time': '2020-01-02',
        'organizer': 'he',
        'start_time': '2020-01-05',
        'address': 'an hui',
        'arrangement': 'Day1: nothing',
        'price': 100,
        'people_number_limit': 50,
        'current_people_number': 10}]

    def setUp(self):
        for activity_data in self.activities_data:
            activity = Activity(name=activity_data['name'],
                                enroll_start_time=activity_data['enroll_start_time'],
                                enroll_end_time=activity_data['enroll_end_time'],
                                organizer=activity_data['organizer'],
                                start_time=activity_data['start_time'],
                                address=activity_data['address'],
                                arrangement=activity_data['arrangement'],
                                price=activity_data['price'],
                                current_people_number=activity_data['current_people_number'],
                                people_number_limit=activity_data['people_number_limit'])
            activity.save()

    def test_activity_list(self):
        """
        分页获取活动

        :author: gexuewen
        :date: 2020/01/01
        """
        res = self.client.get(get_url(urls.ACTIVITY, activity_urls.LIST_ACTIVITY),
                              data={
                                  'page': 1,
                                  'page_size': 2
                              })
        result = res.json()
        self.assertEqual(result['code'], result_util.SUCCESS)
