# Generated by Django 5.0.3 on 2024-03-23 13:45

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название кинофильма')),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2100), django.core.validators.MinValueValidator(1900)], verbose_name='Год выпуска')),
                ('length', models.PositiveIntegerField(verbose_name='Продолжительность')),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Рейтинг фильма')),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='movies', to='movies_app.director', verbose_name='Режиссер')),
            ],
        ),
    ]