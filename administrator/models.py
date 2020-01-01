"""
models

:author: gexuewen
:date: 2019/12/28
"""
from django.db import models


class Privilege(models.Model):
    """
    privilege model

    :author: gexuewen
    :date: 2019/12/28
    """
    PRIVILEGE_CHOICE = (
        (1, '已授权'),
        (2, '未授权')
    )
    # 招生管理
    enrollment = models.IntegerField(choices=PRIVILEGE_CHOICE)
    # 学期管理
    semester = models.IntegerField(choices=PRIVILEGE_CHOICE)
    # 活动管理
    activity = models.IntegerField(choices=PRIVILEGE_CHOICE)
    # 学生管理
    student = models.IntegerField(choices=PRIVILEGE_CHOICE)
    # 超级管理员权限标示
    super = models.IntegerField(choices=PRIVILEGE_CHOICE, default=2)


class Administrator(models.Model):
    """
    administrator model

    :author: gexuewen
    :date: 2019/12/28
    """
    # 账号
    account = models.CharField(max_length=30, blank=False)
    # 密码
    password = models.CharField(max_length=128, blank=False)
    # 姓名
    name = models.CharField(max_length=30)
    # 权限
    privilege = models.ForeignKey(Privilege, on_delete=models.CASCADE)
    # 状态
    state = models.IntegerField(default=1)
