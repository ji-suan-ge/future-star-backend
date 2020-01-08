"""
views

:author: lishanZheng
:date: 2019/12/28
"""
import hashlib
import json
from functools import cmp_to_key
from urllib import request as urllib_request

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin
from xpinyin import Pinyin

from clazz.models import Clazz, ClazzStudent
from student.constant.code import INVALID_JS_CODE
from student.constant.student_state import INVALID, NOT_GRADUATE, VALID
from student.models import Student, WechatStudent
from student.serializers import StudentSerializer, CompanySerializer
from student.test.generate.student import get_section
from util import result_util
from util.pagination import CustomPageNumberPagination


class StudentViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    """
    student view set

    :author: lishanZheng
    :date: 2020/01/01
    """
    serializer_class = StudentSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        queryset = Student.objects.filter(state__in=[NOT_GRADUATE, VALID])
        semester_id = self.request.GET.get('semester_id')
        clazz_id = self.request.GET.get('clazz_id')
        name = self.request.GET.get('name')
        if name is not None:
            queryset = queryset.filter(name__contains=name)
        if clazz_id is not None:
            student_set = ClazzStudent.objects.filter(clazz_id=clazz_id)
            student_list = list(student_set.values_list('student_id', flat=True))
            queryset = queryset.filter(id__in=student_list)
        if semester_id is not None:
            clazz_set = Clazz.objects.filter(semester_id=semester_id)
            clazz_id_list = list(clazz_set.values_list('id', flat=True))
            student_set = ClazzStudent.objects.filter(clazz_id__in=clazz_id_list)
            student_list = list(student_set.values_list('student_id', flat=True))
            queryset = queryset.filter(id__in=student_list)
        return queryset

    def get(self, request):
        """
        get student list

        :author: lishanZheng
        :date: 2020/01/01
        """
        page = self.list(request).data
        return result_util.success(page)


class StudentDetailViewSet(UpdateModelMixin,
                           DestroyModelMixin,
                           GenericAPIView):
    """
    student detail view set

    :author: lishanZheng
    :date: 2020/01/02
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'primary_key'

    def delete(self, request, primary_key):
        """
        delete student

        :author: lishanZheng
        :date: 2020/01/02
        """
        self.destroy(request, primary_key)
        return result_util.success_empty()

    def perform_destroy(self, instance):
        instance.state = INVALID
        instance.save()

    def put(self, request, primary_key):
        """
        update student

        :author: lishanZheng
        :date: 2020/01/02
        """
        student = self.get_object()
        if student.id != primary_key:
            pass
        data = request.data
        company_data = data.get("company")

        company_serializer = CompanySerializer(data=company_data,
                                               partial=True,
                                               instance=student.company)
        if company_serializer.is_valid():
            company_serializer.save()
        student_serializer = StudentSerializer(data=data,
                                               partial=True,
                                               instance=student)
        if student_serializer.is_valid():
            student_serializer.save()
        return result_util.success(student_serializer.data)


def cmp(temp1, temp2):
    """
    compare first letter

    :author: lishanZheng
    :date: 2020/01/08
    """
    if get_letter(temp1.name[0]) < get_letter(temp2.name[0]):
        return -1
    return 1


def get_letter(name):
    """
    get first letter

    :author: lishanZheng
    :date: 2020/01/08
    """
    pinyin = Pinyin()
    if name == '':
        return 'Z'
    letter = pinyin.get_initials(name, u'')[0]
    return letter


class StudentLetterViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):
    """
    student view set

    :author: lishanZheng
    :date: 2020/01/01
    """
    serializer_class = StudentSerializer

    def get(self, request):
        """
        get student list by letter

        :author: lishanZheng
        :date: 2020/01/07
        """
        queryset = Student.objects.filter(state__in=[NOT_GRADUATE, VALID])
        name = self.request.GET.get('name')
        city = self.request.GET.get('city')
        semester = self.request.GET.get('semester_id')
        if name is not None:
            queryset = queryset.filter(name__contains=name)
        if semester is not None:
            clazz_id = list(Clazz.objects.filter(semester_id=semester)
                            .values_list('id', flat=True))
            student_set = ClazzStudent.objects.filter(clazz_id__in=clazz_id)
            student_id = list(student_set.values_list('student_id', flat=True))
            queryset = queryset.filter(id__in=student_id)
        if city is not None:
            student_set = Student.objects.filter(city__contains=city)
            student_id = list(student_set.values_list('id', flat=True))
            queryset = queryset.filter(id__in=student_id)
        queryset = sorted(queryset, key=cmp_to_key(cmp))

        student_list = classifier(queryset)
        data = {
            'count': len(queryset),
            'results': student_list
        }
        return result_util.success(data)


def classifier(student_set):
    """
    按字母分类组织

    :author: lishanZheng
    :date: 2020/01/07
    """
    student_list = []
    times = len(student_set)
    current_letter = ''
    for i in range(times):
        letter = get_letter(student_set[i].name)
        if len(student_list) != 0:
            current_letter = student_list[len(student_list) - 1]['letter']
        student_serializer_data = StudentSerializer(student_set[i]).data
        if current_letter == letter:
            section = student_list[len(student_list) - 1]
            group = section['group']
            group.append(student_serializer_data)
        else:
            section = get_section()
            section['letter'] = letter
            section['group'].append(student_serializer_data)
            student_list.append(section)
    return student_list


@csrf_exempt
def login(request):
    """
    student login

    :author: gexuewen
    :date: 2020/01/06
    """
    app_id = settings.WECHAT_APP_ID
    secret = settings.WECHAT_SECRET
    code = request.POST.get('code')
    url = 'https://api.weixin.qq.com/sns/jscode2session?' \
          'appid=%s&' \
          'secret=%s&' \
          'js_code=%s&' \
          'grant_type=authorization_code' % (app_id, secret, code)
    with urllib_request.urlopen(url) as res:
        result = json.loads(res.read().decode('utf-8'))
    if 'errcode' in result:
        return result_util.error(INVALID_JS_CODE, result.get('errmsg'))
    open_id = result.get('openid')
    session_key = result.get('session_key')
    session_id = open_id + app_id
    md5 = hashlib.md5()
    md5.update(session_id.encode('utf-8'))
    session_id = md5.hexdigest()
    try:
        wechat_student = WechatStudent.objects.get(open_id=open_id)
    except WechatStudent.DoesNotExist:
        wechat_student = None
    if wechat_student is None:
        WechatStudent.objects.create(open_id=open_id,
                                     session_key=session_key,
                                     session_id=session_id,
                                     student=None
                                     )
    else:
        wechat_student.session_key = session_key
        wechat_student.save()
    return result_util.success({'session_id': session_id})
