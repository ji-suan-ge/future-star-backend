"""
models

:author: lishanZheng
:date: 2019/12/28
"""
from django.db import models


class Course(models.Model):
    """
    course

    :author: lishanZheng
    :date: 2019/12/28
    """
    class_id = models.IntegerField(blank=False)  # 课程id
    teacher_id = models.IntegerField(blank=False)  # 老师id
    name = models.CharField(max_length=30, blank=False)  # 课程名字
    introduction = models.TextField()  # 课程介绍
    location = models.CharField(max_length=30)  # 上课地址
    begin_time = models.DateField()  # 课程开始时间
    end_time = models.DateField()  # 课程结束时间


class Content(models.Model):  # 课程条目
    """
    content

    :author: lishanZheng
    :date: 2019/12/28
    """
    course_id = models.IntegerField(blank=False)  # 条目id
    content_name = models.CharField(max_length=30, blank=False)  # 条目名称


class Resource(models.Model):  # 课程资料
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
    content_id = models.IntegerField(blank=False)  # 目录id
    type = models.CharField(max_length=30, blank=False, choices=TYPE_CHOICE)  # 资料的类型
    name = models.CharField(max_length=30, blank=False)  # 资料的名字
    url = models.CharField(max_length=30)
    word = models.TextField()


class Teacher(models.Model):
    """
    Teacher

    :author: lishanZheng
    :date: 2019/12/28
    """
    name = models.CharField(max_length=30, blank=False)  # 老师名字
    avatar = models.CharField(max_length=100)  # 头像
    title = models.CharField(max_length=30)  # 老师的头衔
    introduction = models.TextField()  # 介绍
    contact_way = models.CharField(max_length=30)  # 联系方式
