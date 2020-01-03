"""
activity clazz add test

:author: gexuewen
:date: 2020/01/03
"""
from django.test import TestCase

from activity.models import Activity
from activity.test.generate.activity import get_activity_data
from clazz.models import Clazz
from clazz.test.generate.clazz import get_clazz_data
from semester.models import Semester
from semester.test.generate.semester import get_semester_data
from util import result_util


class TestActivityClazzAdd(TestCase):
    """
    班级加入活动测试

    :author: gexuewen
    :date: 2020/01/03
    """

    def setUp(self):
        semester_data = get_semester_data()
        semester = Semester.objects.create(**semester_data)
        self.clazz_data = get_clazz_data()
        self.clazz = Clazz.objects.create(semester=semester, **self.clazz_data)
        self.activity_data = get_activity_data()
        self.activity = Activity.objects.create(**self.activity_data)

    def test_activity_clazz_join(self):
        """
        加入班级

        :author: gexuewen
        :date: 2020/01/03
        """
        res = self.client.post('/activity/clazz',
                               data={
                                   'activity_id': self.activity.id,
                                   'clazz_id': self.clazz.id
                               })
        result = res.json()
        self.assertEqual(result.get('code'), result_util.SUCCESS)
        data = result.get('data')
        activity = data.get('activity')
        self.assertEqual(activity.get('id'), self.activity.id)
        clazz = data.get('clazz')
        self.assertEqual(clazz.get('id'), self.clazz.id)
