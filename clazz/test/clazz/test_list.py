"""
clazz list test

:author: gexuewen
:date: 2020/01/04
"""
from django.test import TestCase

from clazz.constant.clazz_student_state import WAIT_FOR_AUDIT
from clazz.models import Clazz, ClazzStudent
from clazz.test.generate.clazz import get_clazz_data
from semester.models import Semester
from semester.test.generate.semester import get_semester_data
from student.test.generate.application import get_application_information
from student.test.generate.evaluation import get_evaluation
from student.test.generate.student import get_student


class TestClazzList(TestCase):
    """
    分页获取班级测试

    :author: gexuewen
    :date: 2020/01/04
    """

    def setUp(self):
        self.student = get_student()
        self.another_student = get_student()

        semester_data = get_semester_data()
        self.semester = Semester.objects.create(**semester_data)
        another_semester_data = get_semester_data()
        self.another_semester = Semester.objects.create(**another_semester_data)

        self.clazzes = []
        while len(self.clazzes) < 5:
            clazz_data = get_clazz_data()
            clazz = Clazz.objects.create(semester=self.semester, **clazz_data)
            self.clazzes.append(clazz)
        self.another_clazzes = []
        while len(self.another_clazzes) < 7:
            clazz_data = get_clazz_data()
            clazz = Clazz.objects.create(semester=self.another_semester, **clazz_data)
            self.another_clazzes.append(clazz)
        data = {
            'apply': get_application_information(),
            'evaluation': get_evaluation(),
            'state': WAIT_FOR_AUDIT,
            'student': self.student
        }
        for clazz in self.clazzes[:-2]:
            data['clazz'] = clazz
            ClazzStudent.objects.create(**data)
        data['student'] = self.another_student
        for clazz in self.clazzes[-2:]:
            data['clazz'] = clazz
            ClazzStudent.objects.create(**data)

    def test_activity_list(self):
        """
        分页获取活动

        :author: gexuewen
        :date: 2020/01/01
        """
        data = {
            'page': 2,
            'page_size': 2,
            'semester_id': self.another_semester.id
        }
        res = self.client.get('/clazz/clazz', data=data)
        self.check_result_equal(res, 2, 0, self.another_clazzes[2])
        data['page'] = 4
        res = self.client.get('/clazz/clazz', data=data)
        self.check_result_equal(res, 1, 0, self.another_clazzes[-1])
        data['semester_id'] = self.semester.id
        data['student_id'] = self.student.id
        data['page'] = 2
        res = self.client.get('/clazz/clazz', data=data)
        self.check_result_equal(res, 1, 0, self.clazzes[2])

    def check_result_equal(self, res, length, index, source):
        """
        检查结果是否相符

        :author: gexuewen
        :date: 2020/01/08
        """
        results = res.json().get('data').get('results')
        self.assertEqual(len(results), length)
        clazz = results[index]
        self.assertEqual(source.name, clazz.get('name'))
