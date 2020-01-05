"""
modify teacher test

:author: lishanZheng
:date: 2019/12/28
"""
from django.test import TestCase
from course.test.generate.teacher import get_teacher, get_teacher_data
from util.result_util import SUCCESS


class TestModifyTeacher(TestCase):
    """
    修改老师测试

    :author: lishanZheng
    :date: 2020/01/04
    """
    def test_modify_teacher(self):
        """
        修改老师

        :author: lishanZheng
        :date: 2020/01/04
        """
        teacher_old = get_teacher()
        teacher_data_new = get_teacher_data()
        result_modified_teacher = self.client.put('/course/teacher/' + str(teacher_old.id),
                                                  data=teacher_data_new,
                                                  content_type='application/json')
        result = result_modified_teacher.json()
        code = result.get('code')
        modified_teacher = result.get('data')
        self.assertEqual(code, SUCCESS)
        self.assertEqual(modified_teacher.get('name'), teacher_data_new.get('name'))
        self.assertEqual(modified_teacher.get('avatar'), teacher_data_new.get('avatar'))
        self.assertEqual(modified_teacher.get('title'), teacher_data_new.get('title'))
        self.assertEqual(modified_teacher.get('introduction'), teacher_data_new.get('introduction'))
        self.assertEqual(modified_teacher.get('contact_way'), teacher_data_new.get('contact_way'))
