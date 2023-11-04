from django.db import models

# Create your models here.
class Link(models.Model):
    link = models.CharField('Ссылка на Youtube видео', max_length=250)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
