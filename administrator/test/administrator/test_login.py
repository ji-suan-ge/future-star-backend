"""
administrator login test

:author: lishanZheng
:date: 2020/01/06
"""
from django.test import TestCase

from administrator import code
from administrator.test.generate.administrator import get_administrator
from util.result_util import SUCCESS


class TestAdministratorLogin(TestCase):
    """
    管理员登录测试

    :author: lishanZheng
    :date: 2020/01/06
    """

    def setUp(self):
        self.admin = get_administrator()

    def test_login(self):
        """
        登录成功

        :author: lishanZheng
        :date: 2019/12/30
        """
        res = self.client.post('/administrator/login',
                               data={'account': self.admin.account, 'password': '123'})
        self.assertEqual(res.json()['code'], SUCCESS)

    def test_login_password_error(self):
        """
        登录密码错误

        :author: lishanZheng
        :date: 2019/12/30
        """
        res = self.client.post('/administrator/login',
                               data={'account': self.admin.account, 'password': '1234'})
        self.assertEqual(res.json()['code'], code.INCORRECT_PASSWORD)

    def test_login_not_exist(self):
        """
        登录用户名不存在

        :author: lishanZheng
        :date: 2019/12/30
        """
        res = self.client.post('/administrator/login',
                               data={'account': 'not', 'password': '123'})
        self.assertEqual(res.json()['code'], code.ADMIN_NOT_EXIST)

    def test_logout(self):
        """
        成功登出

        :author: lishanZheng
        :date: 2019/12/30
        """
        self.client.post('/administrator/login',
                         data={'account': self.admin.account, 'password': '123'})
        res = self.client.post('/administrator/logout')
        self.assertEqual(res.json()['code'], SUCCESS)

    def test_not_login(self):
        """
        未登录就登出

        :author: lishanZheng
        :date: 2019/12/30
        """
        res = self.client.post('/administrator/logout',
                               data={})
        self.assertEqual(res.json()['code'], code.NOT_LOGIN)
