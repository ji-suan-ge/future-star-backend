"""
models

:author: lishanZheng
:date: 2019/12/28
"""
from django.db import models


class Semester(models.Model):
    """
    semester

    :author: lishanZheng
    :date: 2019/12/28
    """
    STATE = (
        (0, '正在进行'),
        (1, '已结束')
    )
    # 期数
    period_semester = models.IntegerField()
    # 主题
    subject = models.TextField()
    # 介绍
    introduction = models.TextField()
    state = models.IntegerField(choices=STATE, default=0)
