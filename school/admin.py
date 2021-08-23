from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple
from .models import Head, Tutor, Offices, Subjects, Features

# Register your models here.
class HeadAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)

class TutorAdmin(admin.ModelAdmin):
    list_display = ('l_name', 'f_name', 'office', 'school',)
    list_filter = ('office', 'subject', 'school',)
    formfield_overrides = {
            models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active',)



admin.site.register(Head, HeadAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Offices, OfficeAdmin)
admin.site.register(Subjects, SubjectAdmin)
admin.site.register(Features, FeatureAdmin)
