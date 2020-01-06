"""
modify course test

:author: lishanZheng
:date: 2020/01/05
"""
from django.test import TestCase

from course.test.generate.course import get_course, get_course_data
from util.result_util import SUCCESS


class TestModifyCourse(TestCase):
    """
    修改课程测试

    :author: lishanZheng
    :date: 2020/01/05
    """

    def test_modify_course(self):
        """
        修改课程

        :author: lishanZheng
        :date: 2020/01/05
        """
        course_data = get_course_data()
        course_old = get_course()
        result_modify = self.client.put('/course/course/' + str(course_old.id),
                                        data=course_data,
                                        content_type='application/json')
        res = result_modify.json()
        modified_course = res.get('data')
        self.assertEqual(res.get('code'), SUCCESS)
        self.assertEqual(modified_course.get('name'), course_data.get('name'))
        self.assertEqual(modified_course.get('introduction'), course_data.get('introduction'))
        self.assertEqual(modified_course.get('location'), course_data.get('location'))
