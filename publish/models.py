from django.db import models
from django.utils.translation import ugettext_lazy as _
from authorize.models import User

class Report(models.Model):
    title = models.CharField(_('Название'), max_length=500, blank=True)
    body = models.TextField(_('Текст'), blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name='post_author', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Like(models.Model):
    like_author = models.ForeignKey(User, related_name='like_author', on_delete=models.CASCADE)
    like_post = models.ForeignKey(Report, related_name='like_post', on_delete=models.CASCADE)
    like = models.SmallIntegerField(default=0)
    like_created = models.DateField(format('%Y-%m-%d'), auto_now_add=True)

    def __str__(self):
        return self.like_post.title

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


class Dislike(models.Model):
    dislike_author = models.ForeignKey(User, related_name='dislike_author', on_delete=models.CASCADE)
    dislike_post = models.ForeignKey(Report, related_name='dislike_post', on_delete=models.CASCADE)
    dislike = models.SmallIntegerField(default=0)
    dislike_created = models.DateField(format('%Y-%m-%d'), auto_now_add=True)

    def __str__(self):
        return self.dislike_post.title

    class Meta:
        verbose_name = 'Дизлайк'
        verbose_name_plural = 'Дизлайки'
