"""
用户模型
继承 Django AbstractUser，方便后续扩展自定义字段
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """自定义用户模型"""
    nickname = models.CharField('昵称', max_length=50, blank=True, default='')
    phone = models.CharField('手机号', max_length=20, blank=True, default='')
    avatar = models.URLField('头像', blank=True, default='')

    class Meta:
        db_table = 'users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
