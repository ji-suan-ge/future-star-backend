"""
models

:author: lishanZheng
:date: 2019/12/28
"""
from django.db import models

from clazz.models import Clazz


class Teacher(models.Model):
    """
    Teacher

    :author: lishanZheng
    :date: 2019/12/28
    """
    # 老师名字
    name = models.CharField(max_length=30, blank=False)
    # 头像
    avatar = models.CharField(max_length=100)
    # 老师的头衔
    title = models.CharField(max_length=30)
    # 介绍
    introduction = models.TextField()
    # 联系方式
    contact_way = models.CharField(max_length=30)


class Course(models.Model):
    """
    course

    :author: lishanZheng
    :date: 2019/12/28
    """
    # 课程
    clazz = models.ForeignKey(Clazz, on_delete=models.CASCADE)
    # 老师
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # 课程名字
    name = models.CharField(max_length=30, blank=False)
    # 课程介绍
    introduction = models.TextField()
    # 上课地址
    location = models.CharField(max_length=30)
    # 课程开始时间
    begin_time = models.DateField()
    # 课程结束时间
    end_time = models.DateField()
    # 课程状态
    state = models.IntegerField(default=1)


class Content(models.Model):  # 课程条目
    """
    content

    :author: lishanZheng
    :date: 2019/12/28
    """
    # 条目
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # 条目名称
    content_name = models.CharField(max_length=30, blank=False)


class Resource(models.Model):
    """
    resource

    :author: lishanZheng
    :date: 2019/12/28
    """
    TYPE_CHOICE = (
        (0, '文本'),
        (1, 'PPT'),
        (2, '视频')
    )
    STATE = (
        (0, '开放'),
        (1, '关闭')
    )
    # 目录
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    # 资料的类型
    type = models.CharField(max_length=30, blank=False, choices=TYPE_CHOICE)
    # 资料的名字
    name = models.CharField(max_length=30, blank=False)
    url = models.CharField(max_length=30)
    word = models.TextField()
    state = models.IntegerField(default=1, blank=False, choices=STATE)
