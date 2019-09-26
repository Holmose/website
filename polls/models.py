import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField("问题名称", max_length=200)
    pub_date = models.DateTimeField('创建日期')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'# 根据pub_date排序
    was_published_recently.boolean = True
    was_published_recently.short_description = '最近发布？'
    
    def __str__(self):
        return self.question_text
    class Meta:
        verbose_name = "问题"
        verbose_name_plural = verbose_name

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    class Meta:
        verbose_name = "选择"
        verbose_name_plural = verbose_name
