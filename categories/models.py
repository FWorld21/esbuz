from django.db import models
from django.urls import reverse
from .ru_to_eng import translate


class Categories(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', blank=False)
    title_uz = models.CharField(max_length=150, verbose_name='Название (УЗБ)', blank=False)
    img = models.ImageField(upload_to='media', verbose_name='Картинка', blank=False)
    slug = models.CharField(max_length=300, verbose_name='URL (Необязательно)', blank=True)

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse('products', args=[self.slug])

    def get_url_uz(self):
        return reverse('products', args=[self.slug, 'uz'])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = translate(self.title)
        super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название товара', blank=False)
    name_uz = models.CharField(max_length=300, verbose_name='Название товара (УЗБ)', blank=False)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, default=0)
    model = models.CharField(max_length=300, verbose_name='Модель товара', blank=True)
    product_slug = models.CharField(max_length=300, verbose_name='URL (Необязательно)', blank=True)
    img = models.ImageField(upload_to='media', verbose_name='Картинка', blank=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('about_product', args=[self.category.slug, self.product_slug])

    def get_url_uz(self):
        return reverse('about_product', args=[self.category.slug, self.product_slug, 'uz'])

    def save(self, *args, **kwargs):
        if not self.product_slug:
            self.product_slug = translate(self.name)
        super().save(*args, **kwargs)


class ProductDescription(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Заголовок описания')
    title_uz = models.CharField(max_length=200, verbose_name='Заголовок описания (УЗБ)')
    description = models.TextField(verbose_name='Описание товара')
    description_uz = models.TextField(verbose_name='Описание товара (УЗБ)')

    class Meta:
        verbose_name = 'Описание'
        verbose_name_plural = 'Описания'


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
