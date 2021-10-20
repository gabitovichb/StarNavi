from django.db import models
from django.utils.translation import ugettext_lazy as _
from authorize.models import User

class Report(models.Model):
    title = models.CharField(_('Название'), max_length=500, blank=True)
    body = models.TextField(_('Текст'), blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, related_name='post_author', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
