from django.db import models
from django.utils.safestring import mark_safe
from tinymce import models as tinymce_models
from django.utils import timezone
import os

# Create your models here.
class Head(models.Model):
    title = models.CharField('Title страницы', max_length=120, blank=True, default='100 баллов')
    title_on_image = models.CharField('Заголовок на главном фото', max_length=50, blank=True, default='100 баллов')
    logo = models.CharField('Лого', max_length=30, blank=True, default='Центр "100 баллов"')
    image = models.FileField('Главное фото', blank=True, default='site/images/bg.jpg')

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
    avatar = models.FileField('Логотип', blank=True, default='https://www.100ballov.by/media/django-summernote/2021-08-23/7043d218-16f1-4d13-8152-e4b85320bc78.png', upload_to='tutors')
    link = models.CharField('Ссылка на профиль', max_length=128, blank=True, null=True)
    office = models.ManyToManyField('Offices', verbose_name='Филиал', null=True)
    subject = models.ManyToManyField('Subjects', verbose_name='Предмет', related_name='Предметы')
    school = models.BooleanField('Работает в школе', db_index=True, blank=True, null=True, default=False)
    is_admin = models.BooleanField('Администрация школы', db_index=True, blank=True, null=True, default=False)

    class Meta:
        ordering = ['l_name']
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return f'{self.f_name} {self.l_name}'

class Offices(models.Model):
    name = models.CharField('Филиал', max_length=100, blank=True)
    map_url = models.URLField('Ссылка на карту', max_length=128, blank=True, null=True)

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
    order = models.IntegerField('Порядковый номер отображения', default=9)
    text = tinymce_models.HTMLField('Текст фишки', max_length=7000, blank=True, null=True, db_index=True)
    is_active = models.BooleanField('Активно', db_index=True, blank=True, null=True, default=False)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Фишка'
        verbose_name_plural = 'Фишки'

    def __str__(self):
        return self.title
        

class Forms(models.Model):
    form = models.IntegerField('Класс')

    class Meta:
        ordering = ['form',]
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'

    def __str__(self):
        return f'{self.form} класс'


class Lessons(models.Model):
    subject = models.ForeignKey('Subjects', verbose_name='Предмет', on_delete=models.CASCADE)
    tutor = models.ForeignKey('Tutor', verbose_name='Учитель', on_delete=models.CASCADE)
    office = models.ForeignKey('Offices', verbose_name='Филиал', on_delete=models.CASCADE)
    day = models.CharField('День проведения', max_length=50, null=True)
    time = models.TimeField('Время проведения', default='10:00')
    duration = models.CharField('Продолжительность:', max_length=10, default='45 минут')
    is_active = models.BooleanField('Активно', db_index=True, blank=True, null=True, default=False)
    forms = models.ManyToManyField('Forms', verbose_name='Класс', related_name='Классы')
    link = models.URLField('Ссылка на запись', max_length=300, db_index=True, blank=True, null=True)
    description = tinymce_models.HTMLField('Описание курса', max_length=7000, default='Описание курса появится позже. Следите за обновлениями.')

    class Meta:
        ordering = ['subject', 'day']
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'

    def __str__(self):
        return f'{self.subject} {self.tutor.l_name} {self.day} {self.time}'