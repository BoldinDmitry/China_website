from django.db import models


class Quote(models.Model):
    text = models.TextField(verbose_name="Текст цитаты")
    author = models.CharField(max_length=200, verbose_name="Имя автора")

    def __str__(self):
        return f"{self.author}: {self.text}"
