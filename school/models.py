from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
import os

# Create your models here.
class Head(models.Model):
    title = models.CharField('Title страницы', max_length=120, blank=True, default='100 баллов')
    title_on_image = models.CharField('Заголовок на главном фото', max_length=50, blank=True, default='100 баллов')
    logo = models.CharField('Лого', max_length=30, blank=True, default='Центр "100 баллов"')
    image = models.FileField('Главное фото', blank=True, default='static/site/images/bg.jpg')

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Верхняя часть с фото'
        verbose_name_plural = 'Верхняя часть с фото'

    def __str__(self):
        return self.logo

class Tutor(models.Model):
    l_name = models.CharField('Фамилия', max_length=100, default='', db_index=True, blank=True)
    f_name = models.CharField('Имя', max_length=100, default='', blank=True)
    fath_name = models.CharField('Отчество', max_length=100, default='', blank=True, null=True)
    img_link = models.URLField('Ссылка на фото', max_length=128, db_index=True, blank=True, null=True)
    avatar = models.FileField('Логотип', blank=True, default='static/site/images/tutor_default.jpg', upload_to='tutors')
    link = models.CharField('Ссылка на профиль', max_length=128, blank=True, null=True)
    office = models.ForeignKey('Offices', verbose_name='Филиал', null=True, on_delete=models.CASCADE)
    subject = models.ManyToManyField('Subjects', related_name='Предметы')
    school = models.BooleanField('Работает в школе', db_index=True, blank=True, null=True, default=False)

    class Meta:
        ordering = ['l_name', 'office']
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return f'{self.f_name} {self.l_name}'

class Offices(models.Model):
    name = models.CharField('Филиал', max_length=100, blank=True)

    class Meta:
        ordering = ['name',]
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'

    def __str__(self):
        return self.name

class Subjects(models.Model):
    subj_code = models.CharField('Код предмета', max_length=4, blank=True)
    name = models.CharField('Предмет', max_length=100, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'

    def __str__(self):
        return self.name

class Features(models.Model):
    icon = models.FileField('Иконка', blank=True,
                            default='static/site/images/tutor_default.jpg',
                            upload_to='icons_features')
    title = models.CharField('Фишка', max_length=100, blank=True, null=True, db_index=True)
    text = models.CharField('Текст фишки', max_length=300, blank=True, null=True, db_index=True)
    is_active = models.BooleanField('Активно', db_index=True, blank=True, null=True, default=False)

    class Meta:
        ordering = ['title']
        verbose_name = 'Фишка'
        verbose_name_plural = 'Фишки'

    def __str__(self):
        return self.name

