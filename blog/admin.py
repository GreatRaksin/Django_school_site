from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'is_active')
    list_filter = ('created_date', 'is_active')


admin.site.register(Post, PostAdmin)
