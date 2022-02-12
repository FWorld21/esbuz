from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    content = models.TextField()


class Comments(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    message = models.TextField(verbose_name='Сообщение')
    public = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return f'Комментарий от {self.name}'


class MetaTags(models.Model):
    title = models.CharField(max_length=300, verbose_name='Title', blank=False)
    title_uz = models.CharField(max_length=300, verbose_name='Title (УЗБ)', blank=False)
    keywords = models.TextField(verbose_name='Keywords (Через запятую/Предложением)', blank=False)
    description = models.TextField(verbose_name='Description', blank=False)

    class Meta:
        verbose_name = 'Мета тег'
        verbose_name_plural = 'Мета теги'

    def __str__(self):
        return self.title
