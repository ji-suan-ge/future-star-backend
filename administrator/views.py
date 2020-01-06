"""
administrator views

:author: gexuewen
:date: 2019/12/28
"""
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import mixins

from administrator import code
from administrator.constant.state import VALID
from administrator.models import Administrator, Privilege
from administrator.serializers import AdministratorSerializer
from util import result_util
from util.encrypt import compare
from util.pagination import CustomPageNumberPagination


class AdministratorViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):
    """
    administrator view set

    :author: lishanZheng
    :date: 2020/01/01
    """
    queryset = Administrator.objects.filter(state=VALID)
    serializer_class = AdministratorSerializer
    pagination_class = CustomPageNumberPagination

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.privilege = None

    def get(self, request):
        """
        get administrator list

        :author: lishanZheng
        :date: 2020/01/01
        """
        page = self.list(request).data
        return result_util.success(page)

    def post(self, request):
        """
        add administrator

        :author: lishanZheng
        :date: 2019/12/31
        """
        account = request.POST.get('account')
        admin = Administrator.objects.filter(account=account)
        if admin.count() > 0:
            admin_old = Administrator.objects.get(account=account)
            if admin_old.state == 0:
                admin_old.delete()
            else:
                return result_util.error(error_code=code.ADMIN_EXIST, message='此管理员账户已经存在')
        post = request.POST
        data = {
            'enrollment': post.get('enrollment'),
            'semester': post.get('semester'),
            'activity': post.get('activity'),
            'student': post.get('student')
        }
        self.privilege = Privilege.objects.create(**data)
        administrator = self.get_serializer(data=request.data)
        if administrator.is_valid():
            administrator.save()
        return result_util.success(administrator.data)

    def get_serializer_context(self):
        context = super(AdministratorViewSet, self).get_serializer_context()
        context['privilege'] = self.privilege
        return context


class AdministratorDetailViewSet(mixins.UpdateModelMixin,
                                 mixins.DestroyModelMixin,
                                 generics.GenericAPIView):
    """
    administrator detail view set

    :author: lishanZheng
    :date: 2020/01/06
    """
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'primary_key'

    def put(self, request, primary_key):
        """
        update administrator

        :author: lishanZheng
        :date: 2020/01/06
        """
        admin = self.get_object()
        admin.id = primary_key
        privilege_id = admin.privilege_id
        privilege = Privilege.objects.filter(id=privilege_id)
        data = request.data
        privilege.update(**data)
        admin = AdministratorSerializer(admin)
        return result_util.success(admin.data)


@csrf_exempt
def modify(request):
    """
    modify admin privilege

    :author: lishanZheng
    :date: 2020/01/01
    """
    privilege_id = request.POST['privilege_id']
    privilege = Privilege.objects.get(id=privilege_id)
    privilege.activity = request.POST['activity']
    privilege.student = request.POST['student']
    privilege.semester = request.POST['semester']
    privilege.enrollment = request.POST['enrollment']
    privilege.save()
    return result_util.success_empty()


@csrf_exempt
def delete(request):
    """
    delete admin

    :author: lishanZheng
    :date: 2020/01/01
    """
    admin_id = request.POST.get('id')
    try:
        admin = Administrator.objects.get(id=admin_id)
    except Administrator.DoesNotExist:
        return result_util.error(error_code=code.ADMIN_NOT_EXIST, message='该管理员不存在')
    admin.state = 0
    admin.save()
    return result_util.success_empty()


@csrf_exempt
def login(request):
    """
    login

    :author: lishanZheng
    :date: 2019/12/31
    """
    if request.method == 'POST' and request.POST:
        account = request.POST.get('account')
        password = request.POST.get('password')
        correct_password = ''
        admin = ''
        try:
            admin = Administrator.objects.get(account=account)
            correct_password = admin.password
        except Administrator.DoesNotExist:
            return result_util.error(error_code=code.ADMIN_NOT_EXIST, message='管理员不存在')
        if admin.state == 0:
            return result_util.error(error_code=code.ADMIN_NOT_EXIST, message='管理员不存在')
        if compare(password, correct_password):
            if request.session.get('is_login') is None:
                admin.password = ''
                request.session['is_login'] = True
                admin = AdministratorSerializer(admin).data
                request.session['admin'] = admin
                return result_util.success(admin)
            return result_util.error(error_code=code.IS_LOGIN, message='已登录')
        return result_util.error(error_code=code.INCORRECT_PASSWORD, message='密码错误')
    return result_util.error(error_code=code.EMPTY_REQUEST, message='请求体空')


@csrf_exempt
def logout(request):
    """
    logout

    :author: lishanZheng
    :date: 2019/12/31
    """
    if request.session.get('is_login'):
        request.session['is_login'] = None
        request.session['admin'] = None
        return result_util.success_empty()
    return result_util.error(error_code=code.NOT_LOGIN, message='未登录')
