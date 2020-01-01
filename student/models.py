"""
student module models

:author: lishanZheng
:date: 2019/12/28
"""
from django.db import models


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
    # 公司名字
    name = models.CharField(max_length=30, blank=False)
    # 公司网址
    website = models.CharField(max_length=30)
    # 微信公众号
    wx_public = models.CharField(max_length=30)
    # 公司创建时间
    create_time = models.DateField()
    # 公司所在城市
    city = models.CharField(max_length=30)
    # 公司人数
    number_employee = models.IntegerField()
    # 职位
    position = models.CharField(max_length=30)
    # 公司介绍
    introduction = models.TextField()
    # 公司运营数据
    company_data = models.TextField()
    # 公司收入规模
    income_scale = models.CharField(max_length=30)
    # 融资情况
    financing_situation = models.CharField(max_length=30, choices=FINANCING_SITUATION)
    # 公司估值
    value_of_assessment = models.CharField(max_length=20, default='')


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
    # 是否接受缺勤制度
    accept_absence = models.IntegerField(choices=ACCEPT_CHOICE)
    # 申请理由
    reason_application = models.TextField(blank=False)
    # 可以带来的贡献
    contribution_for_us = models.TextField()
    # 获取报名的渠道
    way = models.CharField(max_length=30, choices=WAY_TO_CAMP)


class RecommendationPeople(models.Model):
    """
    recommendation people model

    :author: lishanZheng
    :date: 2019/12/28
    """
    # 申请资料
    information = models.ForeignKey(ApplicationInformation, on_delete=models.CASCADE)
    # 推荐人姓名
    name = models.CharField(max_length=30, blank=False)
    # 推荐人的公司名字
    company = models.CharField(max_length=30, blank=False)
    # 推荐人的职位
    position = models.CharField(max_length=30)


class Evaluation(models.Model):
    """
    evaluation model

    :author: lishanZheng
    :date: 2019/12/28
    """
    # 评价分数
    fraction = models.IntegerField(blank=False)
    # 评价内容
    description = models.TextField(blank=False)


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
    STATE_CHOICE = (
        (0, '不再是校友'),
        (1, '还未毕业的校友'),
        (2, '校友')
    )
    name = models.CharField(max_length=30, blank=False)
    gender = models.IntegerField(default=0, choices=GENDER_CHOICES)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=11, blank=False)
    # 微信号
    wx = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    # 城市
    city = models.CharField(max_length=30)
    # 最高学历
    education = models.CharField(max_length=30, choices=EDUCATION_LIST)
    # 毕业院校 包括时间
    school = models.CharField(max_length=30)
    # 创业前所在公司名称
    previous_company = models.CharField(max_length=30)
    # 创业前职位
    previous_position = models.CharField(max_length=30)
    # 公司
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # 0 -不再是校友 ｜ 1 -还未毕业的校友 ｜2 -校友
    state = models.IntegerField(choices=STATE_CHOICE)
