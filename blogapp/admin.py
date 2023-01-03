from django.contrib import admin
from . import models

class ArticleModelAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'article_name')

admin.site.register(models.ArticleModel, ArticleModelAdmin)
