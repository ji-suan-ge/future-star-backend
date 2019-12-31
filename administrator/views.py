"""
views

:author: gexuewen
:date: 2019/12/28
"""
from django.views.decorators.csrf import csrf_exempt
from administrator import code
from util import result_uitl
from .serializers import AdministratorSerializer
from .models import Administrator


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
        if correct_password == password:
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
