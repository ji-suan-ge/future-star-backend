"""
views

:author: lishanZheng
:date: 2019/12/28
"""
from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from clazz.models import Clazz, ClazzStudent
from student.constant.state import INVALID, NOT_GRADUATE, VALID
from student.models import Student
from student.serializers import StudentSerializer, CompanySerializer
from util import result_util
from util.pagination import CustomPageNumberPagination


class StudentList(mixins.ListModelMixin,
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
        if semester_id is not None:
            if clazz_id is not None:
                student_set = ClazzStudent.objects.filter(clazz_id=clazz_id)
            else:
                clazz_set = Clazz.objects.filter(semester_id=semester_id)
                clazz_id_list = clazz_set_to_list(clazz_set)
                student_set = ClazzStudent.objects.filter(clazz_id__in=clazz_id_list)
            student_list = student_set_to_list(student_set)
            queryset = Student.objects.filter(id__in=student_list,
                                              state__in=[NOT_GRADUATE, VALID])
        if name is not None:
            queryset = Student.objects.filter(name__contains=name)
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


def clazz_set_to_list(clazz_set):
    """
    从班级集合中得到班级id的list

    :author: lishanZheng
    :date: 2020/01/01
    """
    id_list = []
    times = range(len(clazz_set))
    for i in times:
        id_list.append(clazz_set[i].id)
    return id_list


def student_set_to_list(query):
    """
    从学生集合中得到班级id的list

    :author: lishanZheng
    :date: 2020/01/01
    """
    id_list = []
    times = range(len(query))
    for i in times:
        id_list.append(query[i].student_id)
    return id_list
