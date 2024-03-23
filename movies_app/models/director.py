from django.db import models


class Director(models.Model):
    fio = models.CharField(max_length=100, verbose_name='ФИО')
