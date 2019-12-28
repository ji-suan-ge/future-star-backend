"""
student module models

:author: lishanZheng
:date: 2019/12/28
"""
from django.db import models


class Student(models.Model):
    """
    student model

    :author: lishanZheng
    :date: 2019/12/28
    """
    POSITION_LIST = (
        ('F', '创始人'),
        ('CF', '联合创始人'),
        ('P', '董事长'),
        ('CEO', 'CEO'),
        ('Others', '其他'),
    )
    EDUCATION_LIST = (
        ('PhD', '博士'),
        ('MBA', '硕士'),
        ('Bachelor', '本科'),
        ('College', '专科'),
        ('Others', '其他'),
    )
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女'),
    )
    name = models.CharField(max_length=30, blank=False)
    gender = models.IntegerField(default=0, choices=GENDER_CHOICES)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=11, blank=False)
    wx = models.CharField(max_length=30)  # 微信号
    email = models.CharField(max_length=30)
    city = models.CharField(max_length=30)  # 城市
    education = models.CharField(max_length=30, choices=EDUCATION_LIST)  # 最高学历
    school = models.CharField(max_length=30)  # 毕业院校 包括时间
    previous_school = models.CharField(max_length=30)  # 创业前所在公司名称
    previous_position = models.CharField(max_length=30)  # 创业前职位
    company_id = models.IntegerField(blank=False)  # 公司Id
    state = models.IntegerField(default=1)  # 0 -不再是校友 ｜ 1 -还未毕业的校友 ｜2 -校友
    # student_introduction = models.CharField(max_length=1000)  # 学员介绍
    # # user_referee1_message = models.TextField(blank=False)  # 推荐人信息
    # # user_referee2_message = models.TextField()
    # # user_referee3_message = models.TextField()
    # reason_for_join = models.TextField()  # 加入理由
    # contribution_to_others = models.TextField()  # 能为其他人带来什么


class Company(models.Model):
    """
    company model

    :author: lishanZheng
    :date: 2019/12/28
    """
    FINANCING_SITUATION = (
        ('N', '尚未获得融资'),
        ('seed/angel', '已完成种子/天使融资'),
        ('pre-A', '已完成pre-A轮融资'),
        ('A', '已完成A轮融资'),
        ('refuse', '不方便透露'),
        ('others', '其他'),
    )
    name = models.CharField(max_length=30, blank=False)  # 公司名字
    website = models.CharField(max_length=30)  # 公司网址
    the_wx_public = models.CharField(max_length=30)  # 微信公众号
    company_create_time = models.DateField()  # 公司创建时间
    city = models.CharField(max_length=30)  # 公司所在城市
    number_employee = models.IntegerField()  # 公司人数
    position = models.CharField(max_length=30)  # 职位
    introduction = models.TextField()  # 公司介绍
    company_data = models.TextField()   # 公司运营数据
    income_scale = models.CharField(max_length=30)  # 公司收入规模
    financing_situation = models.CharField(max_length=30, choices=FINANCING_SITUATION)  # 融资情况
    value_of_assessment = models.CharField(max_length=20, default='')  # 公司估值


class ApplicationInformation(models.Model):
    """
    application information model

    :author: lishanZheng
    :date: 2019/12/28
    """
    WAY_TO_CAMP = (
        ('wx', '微信朋友圈'),
        ('friend', '朋友推荐'),
        ('Public', '未来之星公众号：EdStars未来同学会'),
        ('web', '好未来官网'),
        ('media', '媒体报道'),
        ('others', '其他'),
    )
    ACCEPT_CHOICE = (
        (0, '接受'),
        (1, '拒绝')
    )
    accept_absence = models.IntegerField(choices=ACCEPT_CHOICE)  # 是否接受缺勤制度
    reason_application = models.TextField(blank=False)  # 申请理由
    contribution_for_us = models.TextField()  # 可以带来的贡献
    way = models.CharField(max_length=30, choices=WAY_TO_CAMP)  # 获取报名的渠道


class RecommendationPeople(models.Model):
    """
    recommendation people model

    :author: lishanZheng
    :date: 2019/12/28
    """
    information_id = models.IntegerField()  # 申请资料Id
    name = models.CharField(max_length=30, blank=False)  # 推荐人姓名
    company = models.CharField(max_length=30, blank=False)  # 推荐人的公司名字
    position = models.CharField(max_length=30)  # 推荐人的职位


class Evaluation(models.Model):
    """
    evaluation model

    :author: lishanZheng
    :date: 2019/12/28
    """
    fraction = models.IntegerField(blank=False)  # 评价分数
    description = models.TextField(blank=False)  # 评价内容
