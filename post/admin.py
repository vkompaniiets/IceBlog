from django.contrib import admin

from post.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')
    list_per_page = 50


admin.site.register(Post, PostAdmin)