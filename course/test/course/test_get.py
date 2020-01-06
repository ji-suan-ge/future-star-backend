"""
get course list test

:author: lishanZheng
:date: 2020/01/05
"""
from django.test import TestCase
from clazz.test.generate.clazz import get_clazz
from course.test.generate.course import get_course
from util.result_util import SUCCESS


class TestGetCourse(TestCase):
    """
    获取课程测试

    :author: lishanZheng
    :date: 2020/01/05
    """

    def setUp(self):
        course = None
        clazz = get_clazz()
        times = 5
        self.times = times
        self.state_open = 1
        self.state_close = 0
        self.old_clazz_id = clazz.id
        # 3个状态为1 2个为0
        for i in range(times):
            course = get_course()
            course.state = self.state_close
            course.clazz_id = clazz.id
            course.save()
            if i < 2:
                course.state = self.state_open
                course.save()
        # 最后一个clazz_id与上面不同
        clazz = get_clazz()
        course.clazz = clazz
        course.save()
        self.new_clazz_id = clazz.id

    def test_get_course(self):
        """
        获取课程

        :author: lishanZheng
        :date: 2020/01/05
        """
        res = self.client.get('/course/course',
                              data={
                                  'page': 3,
                                  'page_size': 2
                              })
        result = res.json()
        code = result.get('code')
        results_course_list = result.get('data').get('results')
        self.assertEqual(code, SUCCESS)
        self.assertEqual(len(results_course_list), 1)

    def test_get_course_by_clazz_id(self):
        """
        获取课程按班级id

        :author: lishanZheng
        :date: 2020/01/05
        """
        res_clazz_id = self.client.get('/course/course',
                                       data={
                                           'page': 1,
                                           'page_size': 2,
                                           'clazz_id': self.new_clazz_id
                                       })
        result_clazz = res_clazz_id.json()
        self.assertEqual(result_clazz.get('code'), SUCCESS)
        results_course_list = result_clazz.get('data').get('results')
        self.assertEqual(len(results_course_list), 1)
        self.assertEqual(results_course_list[0].get('clazz'), self.new_clazz_id)

    def test_get_course_by_clazz_and_state(self):
        """
        获取课程按班级id加状态

        :author: lishanZheng
        :date: 2020/01/05
        """
        res_state = self.client.get('/course/course',
                                    data={
                                        'page': 1,
                                        'page_size': 2,
                                        'clazz_id': self.old_clazz_id,
                                        'state': self.state_close,
                                    })
        result_state = res_state.json()
        results_course_list = result_state.get('data').get('results')
        self.assertEqual(result_state.get('code'), SUCCESS)
        self.assertEqual(len(results_course_list), 2)
        self.assertEqual(results_course_list[1].get('state'), self.state_close)
        self.assertEqual(results_course_list[1].get('clazz'), self.old_clazz_id)
