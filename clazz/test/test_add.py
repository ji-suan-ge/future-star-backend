"""
add clazz test

:author: gexuewen
:date: 2020/01/04
"""
from django.test import TestCase

import util.result_util as result_util
from clazz.test.generate.clazz import get_clazz_data
from semester.models import Semester
from semester.test.generate.semester import get_semester_data


class TestClazzAdd(TestCase):
    """
    添加班级测试

    :author: gexuewen
    :date: 2020/01/04
    """

    def setUp(self):
        self.semester_data = get_semester_data()
        self.semester = Semester.objects.create(**self.semester_data)
        self.clazz_data = get_clazz_data()
        self.clazz_data['semester_id'] = self.semester.id

    def test_add_clazz(self):
        """
        添加班级

        :author: gexuewen
        :date: 2020/01/04
        """
        res = self.client.post('/clazz/clazz',
                               data=self.clazz_data)
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
        clazz = res.get('data')
        self.assertIsNotNone(clazz)
        self.assertEqual(clazz.get('semester').get('id'), self.semester.id)
