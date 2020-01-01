"""
test administrator

:author: lishanZheng
:date: 2020/01/01
"""
from django.test import TestCase
from administrator import code
from administrator.models import Administrator
from util.encrypt import encrypt
from util.result_util import SUCCESS


class AdministratorTest(TestCase):
    """
    管理员模块单元测试

    :author: lishanZheng
    :date: 2019/12/29
    """

    def setUp(self):
        password = 'test123'
        password = encrypt(password)
        admin = Administrator.objects.create(account='test', password=password,
                                             name='admin_test', privilege_id=1)
        admin.save()

    def test_login(self):
        """
        登录成功

        :author: lishanZheng
        :date: 2019/12/30
        """
        res = self.client.post('/administrator/login',
                               data={'account': 'test', 'password': 'test123'})
        self.assertEqual(res.json()['code'], SUCCESS)

    def test_login_password_error(self):
        """
        登录密码错误

        :author: lishanZheng
        :date: 2019/12/30
        """
        # Administrator.objects.create(account='test', password='test123', privilege_id=0)
        res = self.client.post('/administrator/login',
                               data={'account': 'test', 'password': 'test12'})
        # print(res.json()['code'])
        self.assertEqual(res.json()['code'], code.INCORRECT_PASSWORD)

    def test_login_not_exist(self):
        """
        登录用户名不存在

        :author: lishanZheng
        :date: 2019/12/30
        """
        res = self.client.post('/administrator/login',
                               data={'account': 'test1', 'password': 'test12'})
        self.assertEqual(res.json()['code'], code.ADMIN_NOT_EXIST)

    def test_is_login(self):
        """
        重复登录

        :author: lishanZheng
        :date: 2019/12/30
        """
        res = self.client.post('/administrator/login',
                               data={'account': 'test', 'password': 'test123'})
        res = self.client.post('/administrator/login',
                               data={'account': 'test', 'password': 'test123'})
        self.assertEqual(res.json()['code'], code.IS_LOGIN)

    def test_empty_request(self):
        """
        空请求体

        :author: lishanZheng
        :date: 2019/12/30
        """
        res = self.client.post('/administrator/login',
                               data={})
        self.assertEqual(res.json()['code'], code.EMPTY_REQUEST)

    def test_logout(self):
        """
        成功登出

        :author: lishanZheng
        :date: 2019/12/30
        """
        res = self.client.post('/administrator/login',
                               data={'account': 'test', 'password': 'test123'})
        res = self.client.post('/administrator/logout',
                               data={})
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

    def test_add_admin(self):
        """
        添加一个管理员

        :author: lishanZheng
        :date: 2019/12/30
        """
        res = self.client.post('/administrator/add', data={
            'account': 'test1', 'password': 'test123', 'name': 'test',
            'semester': 2, 'activity': 2, 'enrollment': 2, 'student': 2})
        self.assertEqual(res.json()['code'], SUCCESS)

    def test_admin_exist(self):
        """
        管理员账户已经存在

        :author: lishanZheng
        :date: 2019/12/30
        """
        res = self.client.post('/administrator/add', data={
            'account': 'test', 'password': 'test123', 'name': 'test',
            'semester': 2, 'activity': 2, 'enrollment': 2, 'student': 2})
        self.assertEqual(res.json()['code'], code.ADMIN_EXIST)

    def test_delete(self):
        """
        删除管理员

        :author: lishanZheng
        :date: 2019/12/30
        """
        admin = Administrator.objects.create(account='test_delete', password='123',
                                             name='admin_test', privilege_id=1)
        admin.save()
        res = self.client.post('/administrator/delete', data={'id': admin.id})
        self.assertEqual(res.json()['code'], SUCCESS)

    def test_administrator_list(self):
        """
        分页获取管理员

        :author: lishanZheng
        :date: 2020/01/01
        """
        admin = Administrator.objects.create(account='test_delete', password='123',
                                             name='admin_test', privilege_id=1)
        admin.save()
        res = self.client.get('/administrator/list_administrator',
                              data={
                                  'page': 1,
                                  'page_size': 1
                              })
        result = res.json()
        self.assertEqual(result['code'], SUCCESS)
