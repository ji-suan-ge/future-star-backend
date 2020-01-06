"""
modify privilege test

:author: lishanZheng
:date: 2020/01/06
"""
from django.test import TestCase

from administrator.test.generate.administrator import get_administrator
from util.result_util import SUCCESS


class TestModifyPrivilege(TestCase):
    """
    修改权限测试

    :author: lishanZheng
    :date: 2020/01/06
    """

    def test_modify_pri(self):
        """
        修改管理员权限

        :author: lishanZheng
        :date: 2020/01/06
        """
        admin = get_administrator()
        res = self.client.post('/administrator/modify', data={
            'privilege_id': admin.privilege_id, 'semester': 1, 'activity': 1,
            'enrollment': 1, 'student': 1})
        self.assertEqual(res.json()['code'], SUCCESS)
