"""
teacher

:author: lishanZheng
:date: 2019/12/28
"""
from django.test import TestCase

from course.test.generate.content import get_content
from course.test.generate.resource import get_resource_data
from course.test.generate.teacher import get_teacher_data
from util import result_util


class TestTeacher(TestCase):
    """
    添加老师测试

    :author: lishanZheng
    :date: 2020/01/03
    """

    def test_add_teacher(self):
        """
        添加老师

        :author: lishanZheng
        :date: 2020/01/04
        """
        teacher_data = get_teacher_data()
        res = self.client.post('/course/teacher', data=teacher_data)
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
        teacher = res.get('data')
        self.assertIsNotNone(teacher)
        self.assertEqual(teacher.get('name'), teacher_data.get('name'))
        self.assertEqual(teacher.get('avatar'), teacher_data.get('avatar'))
