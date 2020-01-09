"""
activity models

:author: gexuewen
:date: 2019/12/28
"""
from django.db import models

from activity.constant import activity_state, activity_student_state
from clazz.models import Clazz
from student.models import Student


class Activity(models.Model):
    """
    activity model

    :author: gexuewen
    :date: 2019/12/28
    """
    ACTIVITY_STATE_CHOICE = (
        (activity_state.PUBLISHED, '未开始报名'),
        (activity_state.ENROLLING, '报名中'),
        (activity_state.WAIT_FOR_START, '招生结束没开始'),
        (activity_state.UNDERWAY, '进行中'),
        (activity_state.CLOSED, '已结束'),
        (activity_state.CANCELED, '已取消')
    )
    # 活动名
    name = models.CharField(max_length=30)
    # 报名开始时间
    enroll_start_time = models.DateField()
    # 报名结束时间
    enroll_end_time = models.DateField()
    # 主办方
    organizer = models.CharField(max_length=30)
    # 开始时间
    start_time = models.DateField()
    # 活动地址
    address = models.CharField(max_length=100)
    # 活动日程
    arrangement = models.TextField(max_length=1000)
    # 报名费
    price = models.IntegerField()
    # 当前人数
    current_people_number = models.IntegerField(default=0)
    # 人数限制
    people_number_limit = models.IntegerField()
    # 活动状态
    state = models.IntegerField(choices=ACTIVITY_STATE_CHOICE,
                                default=activity_state.PUBLISHED)


class ActivityStudent(models.Model):
    """
    activity student model

    :author: gexuewen
    :date: 2019/12/28
    """
    STATE_CHOICE = (
        (activity_student_state.WAIT_FOR_PAY, 'WAIT_FOR_PAY'),
        (activity_student_state.PAID, 'PAID')
    )
    # 活动
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    # 校友
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # 缴费状态
    state = models.IntegerField(choices=STATE_CHOICE,
                                default=activity_student_state.WAIT_FOR_PAY)


class ActivityClazz(models.Model):
    """
    activity clazz model

    :author: gexuewen
    :date: 2019/12/28
    """
    # 活动
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    # 班级
    clazz = models.ForeignKey(Clazz, on_delete=models.CASCADE)
