from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .director import Director


class Movie(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название кинофильма')
    year = models.PositiveIntegerField(
        verbose_name='Год выпуска',
        validators=[
            MaxValueValidator(2100),
            MinValueValidator(1900)
        ],
    )
    director = models.ForeignKey(
        Director, on_delete=models.RESTRICT,
        related_name='movies', verbose_name='Режиссер',
    )
    length = models.PositiveIntegerField(verbose_name='Продолжительность')
    rating = models.PositiveIntegerField(
        verbose_name='Рейтинг фильма',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
    )

    def __str__(self):
        return f'Movie "{self.title}" by {self.director.fio}'
