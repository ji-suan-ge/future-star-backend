"""
views

:author: lishanZheng
:date: 2019/12/28
"""
from rest_framework import generics
from rest_framework import mixins
from clazz.models import Clazz, ClazzStudent
from student.models import Student
from student.serializers import StudentSerializer
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
        queryset = Student.objects.filter(state__in=[1, 2])
        semester_id = self.request.GET.get('semester_id')
        clazz_id = self.request.GET.get('clazz_id')
        if semester_id is not None:
            if clazz_id is not None:
                student_set = ClazzStudent.objects.filter(clazz_id=clazz_id)
            else:
                clazz_set = Clazz.objects.filter(semester_id=semester_id)
                clazz_id_list = clazz_set_to_list(clazz_set)
                student_set = ClazzStudent.objects.filter(clazz_id__in=clazz_id_list)
            student_list = student_set_to_list(student_set)
            queryset = Student.objects.filter(id__in=student_list, state__in=[1, 2])
        return queryset

    def get(self, request):
        """
        get student list

        :author: lishanZheng
        :date: 2020/01/01
        """
        page = self.list(request).data
        return result_util.success(page)


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
