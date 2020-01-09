"""
content list

:author: lishanZheng
:date: 2020/01/04
"""
from django.test import TestCase

from course.models import Content
from course.test.generate.content import get_content_data
from course.test.generate.course import get_course
from util import result_util


class TestContentList(TestCase):
    """
    条目列表测试

    :author: lishanZheng
    :date: 2020/01/04
    """

    def setUp(self):
        for j in range(2):
            course = get_course()
            self.course = course
            if j < 2:
                pass
            for i in range(3):
                if i < 2:
                    pass
                content_data = get_content_data()
                content = Content(**content_data, course=course)
                content.save()
                self.content = content

    def test_get_content(self):
        """
        分页获取条目列表测试

        :author: lishanZheng
        :date: 2020/01/04
        """
        res = self.client.get('/course/content',
                              data={
                                  'course_id': self.course.id,
                              })
        res = res.json()
        self.assertEqual(res.get('code'), result_util.SUCCESS)
