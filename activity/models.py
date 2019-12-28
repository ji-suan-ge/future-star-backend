"""
models

:author: gexuewen
:date: 2019/12/28
"""
from django.db import models


class Activity(models.Model):
    """
    activity model

    :author: gexuewen
    :date: 2019/12/28
    """
    name = models.CharField(max_length=30, blank=False)
    enroll_start_time = models.DateField(blank=False)
    enroll_end_time = models.DateField(blank=False)
    organizer = models.CharField(max_length=30, blank=False)
    start_time = models.DateField(blank=False)
    address = models.CharField(max_length=100, blank=False)
    arrangement = models.TextField(max_length=1000, blank=False)
    price = models.FloatField(blank=False)
    people_number_limit = models.IntegerField(blank=False)


class ActivityStudent(models.Model):
    """
    activity student model

    :author: gexuewen
    :date: 2019/12/28
    """
    STATE_CHOICE = (
        (0, 'WAIT_FOR_PAY'),
        (1, 'PAID')
    )
    activity_id = models.IntegerField(blank=False)
    student_id = models.IntegerField(blank=False)
    state = models.IntegerField(choices=STATE_CHOICE)


class ActivityClazz(models.Model):
    """
    activity clazz model

    :author: gexuewen
    :date: 2019/12/28
    """
    activity_id = models.IntegerField(blank=False)
    clazz_id = models.IntegerField(blank=False)
