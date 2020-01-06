"""
add administrator test

:author: lishanZheng
:date: 2020/01/06
"""
from django.test import TestCase

from administrator.code import ADMIN_EXIST
from administrator.models import Administrator, Privilege
from administrator.test.generate.administrator import get_administrator_data
from administrator.test.generate.privilege import get_privilege_data
from util.result_util import SUCCESS


class TestAddAdministrator(TestCase):
    """
    添加管理员测试

    :author: lishanZheng
    :date: 2020/01/06
    """

    def test_add_admin(self):
        """
        添加一个管理员

        :author: lishanZheng
        :date: 2020/01/06
        """
        privilege_data = get_privilege_data()
        administrator_data = get_administrator_data()
        res = self.client.post('/administrator/administrator',
                               data={'privilege': privilege_data,
                                     **administrator_data},
                               content_type='application/json')
        self.assertEqual(res.json()['code'], SUCCESS)

    def test_add_admin_exist(self):
        """
        管理员账户已经存在

        :author: lishanZheng
        :date: 2020/01/06
        """
        privilege_data = get_privilege_data()
        privilege = Privilege.objects.create(**privilege_data)
        administrator_data = get_administrator_data()
        Administrator.objects.create(**administrator_data,
                                     privilege=privilege)
        res = self.client.post('/administrator/administrator',
                               data={'privilege': privilege_data,
                                     **administrator_data},
                               content_type='application/json')
        self.assertEqual(res.json()['code'], ADMIN_EXIST)
