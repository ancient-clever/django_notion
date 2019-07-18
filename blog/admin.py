from django.contrib import admin

from blog.models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('views',)


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
