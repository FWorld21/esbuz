# Generated by Django 3.2.8 on 2021-10-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30, verbose_name='Город')),
                ('street', models.CharField(max_length=30, verbose_name='Улица')),
                ('landmark', models.CharField(blank=True, max_length=40, verbose_name='Ориентир')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='EMail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=23, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'email',
                'verbose_name_plural': 'email',
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
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=23, verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Номер телефона',
                'verbose_name_plural': 'Номера телефонов',
            },
        ),
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('img', models.ImageField(upload_to='media', verbose_name='Иконка')),
                ('link', models.TextField(verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Соцсеть',
                'verbose_name_plural': 'Соцсети',
            },
        ),
    ]