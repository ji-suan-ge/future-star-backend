"""
models

:author: gexuewen
:date: 2019/12/28
"""
from django.db import models

from semester.models import Semester
from student.models import Student, ApplicationInformation, Evaluation


class Clazz(models.Model):
    """
    clazz model

    :author: gexuewen
    :date: 2019/12/28
    """
    CLAZZ_STATE_CHOICE = (
        (0, '正在报名'),
        (1, '进行中'),
        (2, '已结束')
    )
    # 学期
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='clazzs')
    # 班级名称
    name = models.CharField(max_length=30, blank=False)
    # 班级介绍
    introduction = models.TextField(max_length=1000, blank=False)
    # 开始时间
    start_time = models.DateField(blank=False)
    # 结束时间
    end_time = models.DateField(blank=False)
    # 人数限制
    people_number_limit = models.IntegerField(blank=False)
    # 当前人数
    current_people_number = models.IntegerField(blank=False)
    # 班级状态
    state = models.IntegerField(choices=CLAZZ_STATE_CHOICE)


class ClazzStudent(models.Model):
    """
    clazz student model

    :author: gexuewen
    :date: 2019/12/28
    """
    CLAZZ_STUDENT_STATE_CHOICE = (
        (0, '待审核'),
        (1, '已拒绝'),
        (2, '已通过'),
        (3, '已毕业'),
        (4, '未能完成')
    )
    # 班级
    clazz = models.ForeignKey(Clazz, on_delete=models.CASCADE)
    # 校友
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # 申请材料
    apply = models.ForeignKey(ApplicationInformation, on_delete=models.CASCADE)
    # 评价
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)
    # 校友状态
    state = models.IntegerField(choices=CLAZZ_STUDENT_STATE_CHOICE)
