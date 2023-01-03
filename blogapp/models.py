from django.contrib.auth.models import User
from django.db import models


class ArticleModel(models.Model):
    article_name = models.CharField(max_length=200, verbose_name='Article Name')
    created = models.DateField(auto_now_add=True, verbose_name = 'CreatedAt')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article_text = models.TextField()

    def __str__(self):
        return self.article_name

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
