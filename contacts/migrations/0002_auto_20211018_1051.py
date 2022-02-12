# Generated by Django 3.2.8 on 2021-10-18 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='city_uz',
            field=models.CharField(default='', max_length=30, verbose_name='Город (УЗБ)'),
        ),
        migrations.AddField(
            model_name='address',
            name='landmark_uz',
            field=models.CharField(blank=True, default='', max_length=40, verbose_name='Ориентир (УЗБ)'),
        ),
        migrations.AddField(
            model_name='address',
            name='street_uz',
            field=models.CharField(default='', max_length=30, verbose_name='Улица (УЗБ)'),
        ),
    ]
