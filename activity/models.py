"""
activity models

:author: gexuewen
:date: 2019/12/28
"""
from django.db import models

from activity.constant.activity_student_state import WAIT_FOR_PAY, PAID
from clazz.models import Clazz
from student.models import Student


class Activity(models.Model):
    """
    activity model

    :author: gexuewen
    :date: 2019/12/28
    """
    # 活动名
    name = models.CharField(max_length=30, blank=False)
    # 报名开始时间
    enroll_start_time = models.DateField(blank=False)
    # 报名结束时间
    enroll_end_time = models.DateField(blank=False)
    # 主办方
    organizer = models.CharField(max_length=30, blank=False)
    # 开始时间
    start_time = models.DateField(blank=False)
    # 活动地址
    address = models.CharField(max_length=100, blank=False)
    # 活动日程
    arrangement = models.TextField(max_length=1000, blank=False)
    # 报名费
    price = models.FloatField(blank=False)
    # 当前人数
    current_people_number = models.IntegerField(blank=False, default=0)
    # 人数限制
    people_number_limit = models.IntegerField(blank=False, default=0)
    # 活动状态
    state = models.IntegerField(default=0)


class ActivityStudent(models.Model):
    """
    activity student model

    :author: gexuewen
    :date: 2019/12/28
    """
    STATE_CHOICE = (
        (WAIT_FOR_PAY, 'WAIT_FOR_PAY'),
        (PAID, 'PAID')
    )
    # 活动
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    # 校友
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # 缴费状态
    state = models.IntegerField(choices=STATE_CHOICE)


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
