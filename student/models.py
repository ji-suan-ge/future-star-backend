"""
student module models

:author: lishanZheng
:date: 2019/12/28
"""
from django.db import models

from student.constant import accept_choice, gender_choice
from student.constant import student_state


class Company(models.Model):
    """
    company model

    :author: lishanZheng
    :date: 2019/12/28
    """
    # FINANCING_SITUATION_CHOICE = (
    #     (finance_situation.S_N, '尚未获得融资'),
    #     (finance_situation.S_S, '已完成种子/天使融资'),
    #     (finance_situation.S_P, '已完成pre-A轮融资'),
    #     (finance_situation.S_A, '已完成A轮融资'),
    #     (finance_situation.SECRET, '不方便透露'),
    #     (finance_situation.OTHER, '其他'),
    # )
    # 公司名字
    name = models.CharField(max_length=30)
    # 公司网址
    website = models.CharField(max_length=500, blank=True, null=True)
    # 微信公众号
    wx_public = models.CharField(max_length=50, blank=True, null=True)
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
    income_scale = models.CharField(max_length=100)
    # 公司估值
    value_of_assessment = models.CharField(max_length=200)
    # 融资情况
    financing_situation = models.CharField(max_length=100)


class ApplicationInformation(models.Model):
    """
    application information model

    :author: lishanZheng
    :date: 2019/12/28
    """
    # WAY_TO_CAMP_CHOICE = (
    #     (way_to_camp.WX, '微信朋友圈'),
    #     (way_to_camp.FRIEND, '朋友推荐'),
    #     (way_to_camp.PUBLIC, '未来之星公众号：EdStars未来同学会'),
    #     (way_to_camp.WEB, '好未来官网'),
    #     (way_to_camp.MEDIA, '媒体报道'),
    #     (way_to_camp.OTHER, '其他'),
    # )
    ACCEPT_CHOICE = (
        (accept_choice.ACCEPT, '接受'),
        (accept_choice.REFUSED, '拒绝')
    )
    # 申请理由
    reason_application = models.TextField()
    # 可以带来的贡献
    contribution_for_us = models.TextField(blank=True, null=True)
    # 获取报名的渠道
    way = models.CharField(max_length=100)
    # 是否接受缺勤制度
    accept_absence = models.IntegerField(choices=ACCEPT_CHOICE,
                                         default=accept_choice.REFUSED)


class RecommendationPeople(models.Model):
    """
    recommendation people model

    :author: lishanZheng
    :date: 2019/12/28
    """
    # 申请资料
    information = models.ForeignKey(ApplicationInformation,
                                    on_delete=models.CASCADE,
                                    related_name="recommendation_peoples")
    # 推荐人姓名
    name = models.CharField(max_length=30)
    # 推荐人的公司名字
    company = models.CharField(max_length=30)
    # 推荐人的职位
    position = models.CharField(max_length=30)


class Evaluation(models.Model):
    """
    evaluation model

    :author: lishanZheng
    :date: 2019/12/28
    """
    # 评价分数
    fraction = models.IntegerField(blank=True, null=True)
    # 评价内容
    description = models.TextField(blank=True, null=True)


class Student(models.Model):
    """
    student model

    :author: lishanZheng
    :date: 2019/12/28
    """
    # POSITION_CHOICE = (
    #     (student_position.F, '创始人'),
    #     (student_position.CF, '联合创始人'),
    #     (student_position.P, '董事长'),
    #     (student_position.CEO, 'CEO'),
    #     (student_position.OTHER, '其他'),
    # )
    # EDUCATION_CHOICE = (
    #     (student_education.PHD, '博士'),
    #     (student_education.MBA, '硕士'),
    #     (student_education.BACHELOR, '本科'),
    #     (student_education.COLLEGE, '专科'),
    #     (student_education.OTHER, '其他'),
    # )
    GENDER_CHOICE = (
        (gender_choice.MALE, '男'),
        (gender_choice.FEMALE, '女'),
    )
    STATE_CHOICE = (
        (student_state.INVALID, '不再是校友'),
        (student_state.NOT_GRADUATE, '还未毕业的校友'),
        (student_state.VALID, '校友')
    )
    name = models.CharField(max_length=30, null=True)
    birthday = models.DateField(null=True)
    avatar_url = models.CharField(max_length=1000)
    phone_number = models.CharField(max_length=11, null=True)
    # 微信号
    wx = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    # 城市
    city = models.CharField(max_length=30, null=True)
    # 毕业院校 包括时间
    school = models.CharField(max_length=100, null=True)
    # 创业前所在公司名称
    previous_company = models.CharField(max_length=30, null=True)
    # 行业
    profession = models.CharField(max_length=100, null=True)
    # 公司
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    # 最高学历
    education = models.CharField(max_length=100, null=True)
    # 创业前职位
    previous_position = models.CharField(max_length=100, null=True)
    # 性别
    gender = models.IntegerField(choices=GENDER_CHOICE, null=True)
    # 校友状态
    state = models.IntegerField(choices=STATE_CHOICE,
                                default=student_state.INVALID)


class WechatStudent(models.Model):
    """
    wechat student model

    :author: gexuewen
    :date: 2020/01/07
    """
    session_id = models.CharField(max_length=200)
    open_id = models.CharField(max_length=200)
    session_key = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
