from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField('Название', max_length=255)
    anons = models.CharField('Анонс', max_length=255)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')
    slug = models.SlugField('Слаг')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'