from django.contrib import admin

from blog.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "postdate", "category")


admin.site.register(Category)
admin.site.register(Blog)
