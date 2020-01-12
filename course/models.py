"""
models

:author: lishanZheng
:date: 2019/12/28
"""
from django.db import models

from clazz.models import Clazz
from course.constant import course_state, resource_state, resource_type


class Teacher(models.Model):
    """
    Teacher

    :author: lishanZheng
    :date: 2019/12/28
    """
    # 老师名字
    name = models.CharField(max_length=30)
    # 头像
    avatar = models.CharField(max_length=1000, blank=True, null=True)
    # 老师的头衔
    title = models.CharField(max_length=30)
    # 介绍
    introduction = models.TextField()
    # 联系方式
    contact_way = models.CharField(max_length=30, blank=True, null=True)


class Course(models.Model):
    """
    course

    :author: lishanZheng
    :date: 2019/12/28
    """
    COURSE_STATE_CHOICE = (
        (course_state.CLOSED, '已关闭'),
        (course_state.OPEN, '开放中')
    )
    # 课程
    clazz = models.ForeignKey(Clazz, on_delete=models.CASCADE)
    # 老师
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # 课程名字
    name = models.CharField(max_length=30)
    # 课程介绍
    introduction = models.TextField()
    # 上课地址
    location = models.CharField(max_length=30)
    # 课程开始时间
    begin_time = models.DateField()
    # 课程结束时间
    end_time = models.DateField()
    # 课程类别
    sort = models.CharField(max_length=100)
    # 图片
    image = models.CharField(max_length=1000,
                             default='https://i.loli.net/2020/01/09/zkinxqPBwbtdvXQ.png')
    # 图标
    icon = models.CharField(max_length=1000,
                            default='https://i.loli.net/2020/01/09/iEZpONujHL4Sc13.png')
    # 课程状态
    state = models.IntegerField(choices=COURSE_STATE_CHOICE,
                                default=course_state.OPEN)


class Content(models.Model):  # 课程条目
    """
    content

    :author: lishanZheng
    :date: 2019/12/28
    """
    # 条目
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # 条目名称
    content_name = models.CharField(max_length=30)


class Resource(models.Model):
    """
    resource

    :author: lishanZheng
    :date: 2019/12/28
    """
    RESOURCE_TYPE_CHOICE = (
        (resource_type.TEXT, '文本'),
        (resource_type.PPT, 'PPT'),
        (resource_type.VIDEO, '视频')
    )
    RESOURCE_STATE_CHOICE = (
        (resource_state.OPEN, '开放'),
        (resource_state.CLOSED, '关闭')
    )
    # 目录
    content = models.ForeignKey(Content,
                                on_delete=models.CASCADE,
                                related_name="resources")
    # 资料的名字
    name = models.CharField(max_length=30)
    # 资源地址
    url = models.CharField(max_length=1000, blank=True, null=True)
    # 文本内容
    word = models.TextField(blank=True, null=True)
    # 资料的类型
    type = models.IntegerField(choices=RESOURCE_TYPE_CHOICE,
                               default=resource_type.TEXT)
    state = models.IntegerField(default=resource_state.OPEN,
                                choices=RESOURCE_STATE_CHOICE)
