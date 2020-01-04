"""
clazz list test

:author: gexuewen
:date: 2020/01/04
"""
from django.test import TestCase

import util.result_util as result_util
from clazz.models import Clazz
from clazz.test.generate.clazz import get_clazz_data
from semester.models import Semester
from semester.test.generate.semester import get_semester_data


class TestClazzList(TestCase):
    """
    分页获取班级测试

    :author: gexuewen
    :date: 2020/01/04
    """

    def setUp(self):
        self.semester_data = get_semester_data()
        self.semester = Semester.objects.create(**self.semester_data)
        self.clazzes_data = []
        for i in range(0, 6):
            if i == -1:
                pass
            self.clazzes_data.append(get_clazz_data())
        for clazz_data in self.clazzes_data:
            Clazz.objects.create(semester=self.semester, **clazz_data)

    def test_activity_list(self):
        """
        分页获取活动

        :author: gexuewen
        :date: 2020/01/01
        """
        res = self.client.get('/clazz/clazz',
                              data={
                                  'page': 2,
                                  'page_size': 2,
                                  'semester_id': self.semester.id
                              })
        result = res.json()
        self.assertEqual(result.get('code'), result_util.SUCCESS)
        data = result.get('data')
        results = data.get('results')
        self.assertEqual(len(results), 2)
        clazz = results[0]
        self.assertEqual(self.clazzes_data[2].get('name'), clazz.get('name'))
