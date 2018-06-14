from django.db import models
from django.contrib.auth.models import User


class WBUser(User):
    GENDER_OPTIONS = (
        (0, '保密'),
        (1, '男'),
        (2, '女'),
    )
    nickname = models.CharField(verbose_name='昵称', max_length=128)
    gender = models.IntegerField(verbose_name='性别', choices=GENDER_OPTIONS, default=0)
    _info = models.TextField(verbose_name='其他信息')

    def __str__(self):
        return self.nickname or self.username


class WBText(models.Model):
    author = models.ForeignKey(WBUser, verbose_name='作者', related_name='ori_wbs')
    msg = models.TextField(verbose_name='微博', max_length=500)

    class Meta:
        verbose_name = '微博'
        verbose_name_plural = '微博'

    def __str__(self):
        return '{msg}...'.format(msg=self.msg[:20])
