from django.db import models
from djrichtextfield.models import RichTextField


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя автора")
    image = models.ImageField(upload_to="authors", verbose_name="Фотография автора")
    description = models.TextField(verbose_name="Должность/регалии автора")

    def __str__(self):
        return f"{self.id}: {self.name}"


class Heading(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    publication_date = models.DateField(auto_now=True, verbose_name="Дата публикации")
    short_text = models.TextField(verbose_name="Короткий текст для описания")
    text = RichTextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")

    def __str__(self):
        return f"{self.id}: {self.title}"


class Image(models.Model):
    image = models.ImageField(upload_to="headings", verbose_name="Изображеие")
    short_description = models.CharField(max_length=200, verbose_name="Короткое описание")

    def __str__(self):
        return f"{self.id}: {self.short_description}"
