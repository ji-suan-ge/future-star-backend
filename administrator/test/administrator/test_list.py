"""
get administrator list test

:author: lishanZheng
:date: 2020/01/06
"""
from django.test import TestCase

from administrator.models import Administrator, Privilege
from administrator.test.generate.administrator import get_administrator_data
from administrator.test.generate.privilege import get_privilege_data
from util.result_util import SUCCESS


class TestAdministratorList(TestCase):
    """
    管理员模块单元测试

    :author: lishanZheng
    :date: 2020/01/06
    """

    def setUp(self):
        privilege_data = get_privilege_data()
        privilege = Privilege.objects.create(**privilege_data)
        administrator_data = get_administrator_data()
        Administrator.objects.create(**administrator_data,
                                     privilege_id=privilege.id)

    def test_administrator_list(self):
        """
        分页获取管理员

        :author: lishanZheng
        :date: 2020/01/01
        """
        result_administrator = self.client.get('/administrator/administrator',
                                               data={
                                                   'page': 1,
                                                   'page_size': 1
                                               })
        administrator = result_administrator.json()
        self.assertEqual(administrator['code'], SUCCESS)
