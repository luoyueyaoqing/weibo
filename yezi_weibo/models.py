from django.db import models
from django.contrib.auth.models import User
import json


class WBUser(User):
    GENDER_OPTIONS = (
        (0, '保密'),
        (1, '男'),
        (2, '女'),
    )
    nickname = models.CharField(verbose_name='昵称', max_length=128, null=True, blank=True)
    gender = models.IntegerField(verbose_name='性别', choices=GENDER_OPTIONS, default=0)
    _info = models.TextField(verbose_name='其他信息', null=True, blank=True)
    followers = models.ManyToManyField('WBUser', verbose_name='关注')

    class Meta:
        verbose_name = '微博用户'
        verbose_name_plural = '微博用户'

    @property
    def info(self):
        return json.loads(self._info)

    def save_user_info(self, info: dict):
        self._info = json.dumps(info)
        self.save()

    def follow(self, user: 'WBUser'):
        self.followers.add(user)
        self.save()

    def __str__(self):
        return self.nickname or self.username


class WBText(models.Model):
    author = models.ForeignKey(WBUser, verbose_name='作者', related_name='ori_wbs')
    msg = models.TextField(verbose_name='微博', max_length=500)

    class Meta:
        verbose_name = '微博文本'
        verbose_name_plural = '微博文本'

    def __str__(self):
        return '{msg}...'.format(msg=self.msg[:20])


class WeiBo(models.Model):
    user = models.ForeignKey(WBUser, verbose_name='用户', related_name='wbs')
    text = models.ForeignKey(WBText, verbose_name='微博内容', related_name='wbs')
    is_del = models.BooleanField(verbose_name='是否删除', default=False)
    time_create = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '个人微博'
        verbose_name_plural = '个人微博'

    def del_this(self):
        self.is_del = True
        self.save()

    def comment_this(self, user: WBUser, text: str):
        comment = Comment.objects.create(target=self, user=user, text=text)
        return comment

    def __str__(self):
        return self.text.msg


class Comment(models.Model):
    user = models.ForeignKey(WBUser, verbose_name='用户', related_name='comments')
    target = models.ForeignKey(WeiBo, verbose_name='被评微博', related_name='comments')
    text = models.TextField(max_length=500, verbose_name="评论")
    is_del = models.BooleanField(verbose_name='是否删除', default=False)
    time_create = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'

    def del_this(self):
        self.is_del = True
        self.save()

    def __str__(self):
        return '{msg}'.format(msg=self.text[:20])