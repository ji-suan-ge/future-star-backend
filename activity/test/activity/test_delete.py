"""
delete activity test

:author: gexuewen
:date: 2020/01/03
"""
from django.test import TestCase

import util.result_util as result_util
from activity.models import Activity
from activity.test.generate.activity import get_activity_data


class TestActivityDelete(TestCase):
    """
    取消活动测试

    :author: gexuewen
    :date: 2020/01/02
    """

    def setUp(self):
        self.activity_data = get_activity_data()
        self.activity = Activity.objects.create(**self.activity_data)

    def test_delete_activity(self):
        """
        取消活动

        :author: gexuewen
        :date: 2020/01/03
        """
        res = self.client.delete('/activity/activity/%d' % self.activity.id)
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
