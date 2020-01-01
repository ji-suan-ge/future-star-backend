"""
views

:author: gexuewen
:date: 2019/12/28
"""
from django.views.decorators.csrf import csrf_exempt
from administrator import code
from util import result_util
from util.encrypt import compare, encrypt
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
        password = encrypt(password)
        name = request.POST.get('name')
        enrollment = request.POST.get('enrollment')
        semester = request.POST.get('semester')
        activity = request.POST.get('activity')
        student = request.POST.get('student')
        admin = Administrator.objects.filter(account=account)
        if admin.count() > 0:
            admin_old = Administrator.objects.get(account=account)
            if admin_old.state == 0:
                admin_old.delete()
            else:
                return result_util.error(error_code=code.ADMIN_EXIST, message='此管理员账户已经存在')
        privilege = Privilege.objects.create(enrollment=enrollment, semester=semester,
                                             activity=activity, student=student, super=2)
        admin = Administrator.objects.create(account=account, password=password,
                                             name=name, privilege_id=privilege.id)
        admin.password = ''
        privilege = PrivilegeSerializer(privilege).data
        admin = AdministratorSerializer(admin).data
        # 合并管理员与权限
        privilege = privilege.copy()
        privilege.update(admin)
        return result_util.success(data=privilege)
    return result_util.error(error_code=code.EMPTY_REQUEST, message='请求体空')


@csrf_exempt
def modify_privilege(request):
    """
    modify admin privilege

    :author: lishanZheng
    :date: 2020/01/01
    """
    if request.method == 'POST' and request.POST:
        privilege_id = request.POST.get('privilege_id')
        enrollment = request.POST.get('enrollment')
        semester = request.POST.get('semester')
        activity = request.POST.get('activity')
        student = request.POST.get('student')
        privilege = Privilege.objects.get(id=privilege_id)
        privilege.enrollment = enrollment
        privilege.semester = semester
        privilege.activity = activity
        privilege.student = student
        privilege.save()
        privilege = PrivilegeSerializer(privilege).data
        return result_util.success(privilege)
    return result_util.error(error_code=code.EMPTY_REQUEST, message='请求体空')


@csrf_exempt
def delete(request):
    """
    delete admin

    :author: lishanZheng
    :date: 2020/01/01
    """
    if request.method == 'POST' and request.POST:
        admin_id = request.POST.get('id')
        try:
            admin = Administrator.objects.get(id=admin_id)
        except Administrator.DoesNotExist:
            return result_util.error(error_code=code.ADMIN_NOT_EXIST, message='该管理员不存在')
        admin.state = 0
        admin.save()
        return result_util.success_empty()
    return result_util.error(error_code=code.EMPTY_REQUEST, message='请求体空')
