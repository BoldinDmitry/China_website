from django.db import models
from djrichtextfield.models import RichTextField


class News(models.Model):
    tag_choices = (
        ("pol", "Политика"),
        ("eco", "Экономика"),
        ("cul", "Культура"),
        ("peo", "Люди"),
        ("arc", "Архитектура"),
        ("lit", "Литература"),
        ("art", "Живопись"),
        ("cin", "Кино"),
    )

    title = models.CharField(max_length=200, verbose_name="Название новости")
    publication_date = models.DateTimeField(auto_now=True)
    short_text = models.TextField(verbose_name="Короткий текст новости")
    text = RichTextField(verbose_name="Длиный текст")
    image = models.ImageField(upload_to="news", verbose_name="Картинка для новости")
    tag = models.CharField(
        max_length=3, verbose_name="Тег новости", choices=tag_choices
    )

    def __str__(self):
        return f"{self.pk}: {self.tag}, {self.title}"
