# Generated by Django 3.2.8 on 2021-10-12 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='media', verbose_name='Картинка'),
        ),
    ]
