from django.contrib import admin

from .models import Post, Tag


class MyAdminSite(admin.AdminSite):
    site_header = 'Monty Python administration'


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'title', 'short_content', 'get_tags', 'get_btn')
    readonly_fields = ('image_preview',)


admin_site = MyAdminSite(name='admin')
admin_site.register(Post, PostAdmin)
admin_site.register(Tag, TagAdmin)
