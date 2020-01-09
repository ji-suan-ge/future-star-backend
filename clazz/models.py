"""
models

:author: gexuewen
:date: 2019/12/28
"""
from django.db import models

from clazz.constant import clazz_state, clazz_student_state
from semester.models import Semester
from student.models import Student, ApplicationInformation, Evaluation


class Clazz(models.Model):
    """
    clazz model

    :author: gexuewen
    :date: 2019/12/28
    """
    CLAZZ_STATE_CHOICE = (
        (clazz_state.UNOPENED, '没有开始招生'),
        (clazz_state.ENROLLING, '招生中'),
        (clazz_state.BEFORE, '招生结束没开课'),
        (clazz_state.UNDERWAY, '开课中'),
        (clazz_state.CLOSED, '已结束')
    )
    # 学期
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='clazzes')
    # 班级名称
    name = models.CharField(max_length=30)
    # 班级介绍
    introduction = models.TextField(max_length=1000)
    # 开始时间
    start_time = models.DateField()
    # 结束时间
    end_time = models.DateField()
    # 人数限制
    people_number_limit = models.IntegerField()
    # 当前人数
    current_people_number = models.IntegerField(default=0)
    # 班级状态
    state = models.IntegerField(choices=CLAZZ_STATE_CHOICE,
                                default=clazz_state.UNOPENED)


class ClazzStudent(models.Model):
    """
    clazz student model

    :author: gexuewen
    :date: 2019/12/28
    """
    CLAZZ_STUDENT_STATE_CHOICE = (
        (clazz_student_state.WAIT_FOR_AUDIT, '待审核'),
        (clazz_student_state.REFUSED, '已拒绝'),
        (clazz_student_state.PASSED, '已通过'),
        (clazz_student_state.GRADUATED, '已毕业'),
        (clazz_student_state.UNABLE_FINISHED, '未能完成')
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
    state = models.IntegerField(choices=CLAZZ_STUDENT_STATE_CHOICE,
                                default=clazz_student_state.WAIT_FOR_AUDIT)
