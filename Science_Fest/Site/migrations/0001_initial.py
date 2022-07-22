# Generated by Django 3.2 on 2022-07-19 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concurs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=255, verbose_name='Название фестиваля')),
                ('description', models.TextField(verbose_name='Описание фестиваля')),
                ('data', models.DateField(verbose_name='Дата проведения')),
            ],
            options={
                'verbose_name': 'Фестиваль',
                'verbose_name_plural': 'Фестивали',
                'ordering': ['id'],
            },
        ),
    ]