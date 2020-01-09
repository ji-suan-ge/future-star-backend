"""
models

:author: gexuewen
:date: 2019/12/28
"""
from django.db import models

from administrator.constant import administrator_state, privilege_state


class Privilege(models.Model):
    """
    privilege model

    :author: gexuewen
    :date: 2019/12/28
    """
    PRIVILEGE_CHOICE = (
        (privilege_state.VALID, '已授权'),
        (privilege_state.INVALID, '未授权')
    )
    # 招生管理
    enrollment = models.IntegerField(choices=PRIVILEGE_CHOICE,
                                     default=privilege_state.INVALID)
    # 学期管理
    semester = models.IntegerField(choices=PRIVILEGE_CHOICE,
                                   default=privilege_state.INVALID)
    # 活动管理
    activity = models.IntegerField(choices=PRIVILEGE_CHOICE,
                                   default=privilege_state.INVALID)
    # 学生管理
    student = models.IntegerField(choices=PRIVILEGE_CHOICE,
                                  default=privilege_state.INVALID)
    # 超级管理员权限标示
    super = models.IntegerField(choices=PRIVILEGE_CHOICE,
                                default=privilege_state.INVALID)


class Administrator(models.Model):
    """
    administrator model

    :author: gexuewen
    :date: 2019/12/28
    """
    ADMINISTRATOR_STATE_CHOICE = (
        (administrator_state.VALID, '活动'),
        (administrator_state.INVALID, '锁定')
    )
    # 账号
    account = models.CharField(max_length=30)
    # 密码
    password = models.CharField(max_length=128)
    # 姓名
    name = models.CharField(max_length=30)
    # 权限
    privilege = models.ForeignKey(Privilege, on_delete=models.CASCADE)
    # 状态
    state = models.IntegerField(choices=ADMINISTRATOR_STATE_CHOICE,
                                default=administrator_state.VALID)
