from django.db import models


class Benefits(models.Model):
    how_time_service_working = models.DecimalField(verbose_name='Сколько лет на рынке?', max_digits=4, decimal_places=0)
    how_many_sold = models.DecimalField(verbose_name='Сколько насосов продано?', max_digits=4, decimal_places=0)
    how_many_reviews = models.DecimalField(verbose_name='Более скольки отзывов?', max_digits=4, decimal_places=0)

    class Meta:
        verbose_name = 'Преимущества'
        verbose_name_plural = 'Преимущества'

    def __str__(self):
        return 'Наши преимущества'


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
