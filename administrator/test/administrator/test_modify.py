"""
modify administrator test

:author: lishanZheng
:date: 2020/01/06
"""
from django.test import TestCase

from administrator.test.generate.administrator import get_administrator, get_administrator_data
from administrator.test.generate.privilege import get_privilege_data
from util.result_util import SUCCESS


class TestModifyPrivilege(TestCase):
    """
    修改管理员信息测试

    :author: lishanZheng
    :date: 2020/01/06
    """

    def test_modify_administrator(self):
        """
        修改管理员权限

        :author: lishanZheng
        :date: 2020/01/06
        """
        admin = get_administrator()
        privilege_data = get_privilege_data()
        administrator_data = get_administrator_data()
        res = self.client.put('/administrator/administrator/' + str(admin.id),
                              data=({
                                  'privilege': privilege_data,
                                  **administrator_data
                              }),
                              content_type='application/json')
        self.assertEqual(res.json()['code'], SUCCESS)
