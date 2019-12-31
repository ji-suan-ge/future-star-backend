"""
views

:author: gexuewen
:date: 2019/12/28
"""
from django.views.decorators.csrf import csrf_exempt
from administrator import code
from util import result_uitl
from util.encrypt import compare
from .serializers import AdministratorSerializer, PrivilegeSerializer
from .models import Administrator, Privilege


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
            return result_uitl.error(error_code=code.ADMIN_NOT_EXIST, message='管理员不存在')
        if compare(password, correct_password):
            if request.session.get('is_login') is None:
                admin.password = ''
                request.session['is_login'] = True
                admin = AdministratorSerializer(admin).data
                request.session['admin'] = admin
                return result_uitl.success(admin)
            return result_uitl.error(error_code=code.IS_LOGIN, message='已登陆')
        return result_uitl.error(error_code=code.INCORRECT_PASSWORD, message='密码错误')
    return result_uitl.error(error_code=code.EMPTY_REQUEST, message='请求体空')


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
        return result_uitl.success_empty()
    return result_uitl.error(error_code=code.NOT_LOGIN, message='未登陆')


@csrf_exempt
def add(request):
    """
    add new admin

    :author: lishanZheng
    :date: 2019/12/31
    """
    if request.method == 'POST' and request.POST:
        account = request.POST.get('account')
        password = request.POST.get('password')
        name = request.POST.get('name')
        enrollment = request.POST.get('enrollment')
        semester = request.POST.get('semester')
        activity = request.POST.get('activity')
        student = request.POST.get('student')
        admin = Administrator.objects.filter(account=account)
        if admin.count() > 0:
            return result_uitl.error(error_code=code.ADMIN_EXIST, message='此管理员账户已经存在')
        privilege = Privilege.objects.create(enrollment=enrollment, semester=semester,
                                             activity=activity, student=student, super=2)
        admin = Administrator.objects.create(account=account, password=password,
                                             name=name, privilege_id=privilege.id)
        privilege = PrivilegeSerializer(privilege).data
        admin = AdministratorSerializer(admin).data
        # 合并管理员与权限
        admin = admin.copy()
        admin.update(privilege)
        return result_uitl.success(data=admin)
    return result_uitl.error(error_code=code.EMPTY_REQUEST, message='请求体空')
