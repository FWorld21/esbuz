# Generated by Django 3.2.8 on 2021-10-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('how_time_service_working', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Сколько лет на рынке?')),
                ('how_many_sold', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Сколько насосов продано?')),
                ('how_many_reviews', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Более скольки отзывов?')),
            ],
            options={
                'verbose_name': 'Преимущества',
                'verbose_name_plural': 'Преимущества',
            },
        ),
        migrations.CreateModel(
            name='MetaTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=300, verbose_name='Title (УЗБ)')),
                ('keywords', models.TextField(verbose_name='Keywords (Через запятую/Предложением)')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Мета тег',
                'verbose_name_plural': 'Мета теги',
            },
        ),
    ]
