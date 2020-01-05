"""
add course test

:author: lishanZheng
:date: 2020/01/05
"""
from django.test import TestCase
from course.test.generate.clazz import get_clazz
from course.test.generate.course import get_course_data
from course.test.generate.teacher import get_teacher_data
from util.result_util import SUCCESS


class TestAddCourse(TestCase):
    """
    添加课程测试

    :author: lishanZheng
    :date: 2020/01/05
    """

    def test_add_course(self):
        """
        添加课程

        :author: lishanZheng
        :date: 2020/01/05
        """
        clazz = get_clazz()
        course_data = get_course_data()
        teacher_data = get_teacher_data()
        course_data['teacher'] = teacher_data
        course_data['clazz'] = clazz.id
        res = self.client.post('/course/course', data=course_data, content_type='application/json')
        result = res.json()
        self.assertEqual(result.get('code'), SUCCESS)
        course = result.get('data')
        self.assertIsNotNone(course)
        self.assertEqual(course.get('name'), course_data.get('name'))
        self.assertEqual(course.get('introduction'), course_data.get('introduction'))
        self.assertEqual(course.get('location'), course_data.get('location'))
