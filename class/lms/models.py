from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Задача')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['updated_at']


class Solution(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Cтудент")
    task = models.ForeignKey(Task, on_delete=models.CASCADE,verbose_name="Задание")
    text = models.TextField(verbose_name="Решение")

    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'


class Mark(models.Model):
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE,verbose_name="Решение")
    mark = models.IntegerField(validators=[
                                            MaxValueValidator(100),
                                            MinValueValidator(1)
                                           ])
    comment = models.TextField(blank=True, null=True, verbose_name="Комментарий")

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'
        ordering = ['-mark']

