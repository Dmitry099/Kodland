from django.db import models
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=100,
                             verbose_name='Название статьи')
    text = models.TextField(verbose_name='Описание статьи')
    published_at = models.DateTimeField(auto_now=True,
                                        verbose_name='Дата публикации')
    image = models.ImageField(upload_to='images/', null=True, blank=True,
                              verbose_name='Загрузить изображение')

    def __str__(self):
        return self.title

    @staticmethod
    def get_absolute_url():
        return reverse('blogs')

    class Meta:
        ordering = ['-published_at']
        db_table = 'posts'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


