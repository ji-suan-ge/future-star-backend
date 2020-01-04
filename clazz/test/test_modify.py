"""
modify clazz test

:author: gexuewen
:date: 2020/01/04
"""
from django.test import TestCase

import util.result_util as result_util
from clazz.models import Clazz
from clazz.test.generate.clazz import get_clazz_data as obtain_clazz_data
from semester.models import Semester
from semester.test.generate.semester import get_semester_data


class TestActivityModify(TestCase):
    """
    修改班级测试

    :author: gexuewen
    :date: 2020/01/04
    """

    def setUp(self):
        self.semester_data = get_semester_data()
        self.semester = Semester.objects.create(**self.semester_data)
        self.clazz_data = obtain_clazz_data()
        self.clazz = Clazz.objects.create(semester=self.semester, **self.clazz_data)
        self.another_semester = Semester.objects.create(**self.semester_data)

    def test_modify_clazz(self):
        """
        修改活班级

        :author: gexuewen
        :date: 2020/01/04
        """
        self.clazz_data['name'] = 'modify name'
        self.clazz_data['current_people_number'] = 3
        self.clazz_data['semester_id'] = self.another_semester.id
        res = self.client.put('/clazz/clazz/' + str(self.clazz.id),
                              data=self.clazz_data,
                              content_type="application/json").json()
        code = res.get('code')
        self.assertEqual(code, result_util.SUCCESS)
        result_clazz = res.get('data')
        self.assertEqual(result_clazz.get('name'),
                         self.clazz_data.get('name'))
        self.assertEqual(result_clazz.get('current_people_number'),
                         self.clazz_data.get('current_people_number'))
        self.assertEqual(result_clazz.get('semester').get('id'),
                         self.another_semester.id)

        self.assertEqual(result_clazz.get('end_time'),
                         self.clazz_data.get('end_time'))
