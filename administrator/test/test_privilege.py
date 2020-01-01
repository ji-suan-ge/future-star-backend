"""
tests

:author: gexuewen
:date: 2019/12/28
"""
from django.test import TestCase
from administrator.models import Administrator, Privilege
from util.encrypt import encrypt
from util.result_util import SUCCESS


class PrivilegeTest(TestCase):
    """
    权限模块单元测试

    :author: lishanZheng
    :date: 2019/12/29
    """

    def setUp(self):
        password = 'test12'
        password = encrypt(password)
        Administrator.objects.create(account='test2', password=password,
                                     name='admin_test', privilege_id=1)

    def test_modify_pri(self):
        """
        修改管理员权限

        :author: lishanZheng
        :date: 2019/12/30
        """
        privilege = Privilege.objects.create(enrollment=2, semester=2,
                                             activity=2, student=2, super=2)
        privilege.save()
        res = self.client.post('/administrator/modify_pri', data={
            'privilege_id': privilege.id, 'semester': 1, 'activity': 1,
            'enrollment': 1, 'student': 1})
        self.assertEqual(res.json()['code'], SUCCESS)
