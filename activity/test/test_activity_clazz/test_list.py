"""
activity clazz list test

:author: gexuewen
:date: 2020/01/03
"""
from django.test import TestCase

from activity.models import Activity, ActivityClazz
from activity.test.generate.activity import get_activity_data
from clazz.models import Clazz
# get as obtain, make pylint happy again
from clazz.test.generate.clazz import get_clazz_data as obtain_clazz_data
from semester.models import Semester
from semester.test.generate.generate import get_semester_data
from util import result_util


class TestActivityClazzList(TestCase):
    """
    分页获取活动班级测试

    :author: gexuewen
    :date: 2020/01/03
    """

    def setUp(self):
        self.activity_clazzes = []
        semester_data = get_semester_data()
        semester = Semester.objects.create(**semester_data)
        self.activity_data = get_activity_data()
        self.activity = Activity.objects.create(**self.activity_data)
        self.clazzes = []
        self.clazzes_data = []
        for i in range(0, 8):
            clazz_data = obtain_clazz_data()
            clazz = Clazz.objects.create(semester=semester, **clazz_data)
            self.clazzes.append(clazz)
            self.clazzes_data.append(clazz_data)
            if i < 5:
                activity_clazz = ActivityClazz.objects.create(
                    activity=self.activity,
                    clazz=self.clazzes[i]
                )
                self.activity_clazzes.append(activity_clazz)

    def test_activity_clazz_list(self):
        """
        分页获取活动班级

        :author: gexuewen
        :date: 2020/01/03
        """
        res = self.client.get('/activity/clazz',
                              data={
                                  'page': 2,
                                  'page_size': 2,
                                  'activity_id': self.activity.id
                              })
        result = res.json()
        self.assertEqual(result.get('code'), result_util.SUCCESS)

        data = result.get('data')
        self.assertIsNotNone(data)

        results = data.get('results')
        self.assertEqual(len(results), 2)
        result_clazz = results[1]
        clazz = self.activity_clazzes[3].clazz
        self.assertEqual(result_clazz.get('id'), clazz.id)
