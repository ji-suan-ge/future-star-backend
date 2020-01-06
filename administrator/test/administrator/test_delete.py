"""
delete administrator test

:author: lishanZheng
:date: 2020/01/06
"""
from django.test import TestCase

from administrator.models import Administrator
from administrator.test.generate.administrator import get_administrator_data
from administrator.test.generate.privilege import get_privilege
from util.result_util import SUCCESS


class TestDeleteAdministrator(TestCase):
    """
    删除管理员测试

    :author: lishanZheng
    :date: 2020/01/06
    """

    def setUp(self):
        privilege = get_privilege()
        administrator_data_delete = get_administrator_data()
        admin = Administrator.objects.create(**administrator_data_delete,
                                             privilege_id=privilege.id)
        self.admin = admin

    def test_delete_administrator(self):
        """
        删除管理员

        :author: lishanZheng
        :date: 2020/01/06
        """
        res = self.client.post('/administrator/delete', data={'id': self.admin.id})
        self.assertEqual(res.json()['code'], SUCCESS)
