from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'content', 'created_at', 'updated_at', 'is_published', 'category', 'photo', 'get_photo', 'views')
    readonly_fields = ('created_at', 'updated_at', 'photo', 'get_photo', 'views')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return 'No image'

    get_photo.short_description = 'Image'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category)

admin.site.site_title = 'Django Administration'
admin.site.site_header = 'Yaropolk Administration'