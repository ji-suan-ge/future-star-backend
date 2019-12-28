from django.db import models

# Create your models here.


class Semester(models.Model):
    STATE = (
        (0, '正在进行'),
        (1, '已结束')
    )
    period_semester = models.IntegerField()
    theme = models.TextField()
    introduction = models.TextField()
    state = models.IntegerField(choices=STATE, default=0)