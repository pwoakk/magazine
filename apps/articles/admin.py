from django.contrib import admin

from .models import Article, ArticleCategory


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    pass