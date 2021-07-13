from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Tag(models.Model):
    topic = models.CharField(max_length=256, verbose_name='Категория')
    articles = models.ManyToManyField(Article, related_name='topics', through='Relationship')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['topic']

    def __str__(self):
        return self.topic


class Relationship(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='статья')
    topic = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='раздел')
    is_main = models.BooleanField(default=False, verbose_name='основной')

    class Meta:
        ordering = ['-is_main', 'topic']
