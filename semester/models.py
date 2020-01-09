"""
models

:author: lishanZheng
:date: 2019/12/28
"""
from django.db import models

from semester.constant import semester_state


class Semester(models.Model):
    """
    semester

    :author: lishanZheng
    :date: 2019/12/28
    """
    SEMESTER_STATE_CHOICE = (
        (semester_state.OPEN, '正在进行'),
        (semester_state.CLOSED, '已结束')
    )
    # 期数
    period_semester = models.IntegerField()
    # 主题
    subject = models.TextField()
    # 介绍
    introduction = models.TextField()
    state = models.IntegerField(choices=SEMESTER_STATE_CHOICE,
                                default=semester_state.OPEN)
