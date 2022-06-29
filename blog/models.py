from django.conf import settings
from django.db import models
from django.utils import timezone
from tinymce import models as tinymce_models


class Post(models.Model):
    title = models.CharField(max_length=200)
    annotation = tinymce_models.HTMLField('Краткий текст', max_length=3000, blank=True, null=True, db_index=True)
    text = tinymce_models.HTMLField('Текст поста', max_length=7000, blank=True, null=True, db_index=True)
    created_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField('Опубликовано', db_index=True, blank=True, null=True, default=False)

    class Meta:
        ordering = ['created_date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def publish(self):
        self.save()

    def __str__(self):
        return self.title