from django.db import models


class Internship(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название стажировки")
    time = models.TextField(verbose_name="Когда?")
    place = models.TextField(verbose_name="Где?")
    city = models.CharField(verbose_name="Город", max_length=50, default="")
    organization = models.TextField(verbose_name="Организация", default="")
    conditions = models.TextField(verbose_name="Условия")
    rating = models.FloatField(verbose_name="Рейтинг")
    description = models.TextField(verbose_name="Описание")

    image1 = models.ImageField(
        verbose_name="Первая картинка", upload_to="internship_images"
    )
    image2 = models.ImageField(
        verbose_name="Вторая картинка", blank=True, upload_to="internship_images"
    )
    image3 = models.ImageField(
        verbose_name="Третья картинка", blank=True, upload_to="internship_images"
    )
    image4 = models.ImageField(
        verbose_name="Четвертая картинка", blank=True, upload_to="internship_images"
    )

    # Not for design
    start = models.DateField(verbose_name="Дата начала стажировки")
    end = models.DateField(verbose_name="Дата конца стажировки")
    is_active = models.BooleanField(verbose_name="Отображать на сайте?")

    def __str__(self):
        return f"{self.pk}: {self.name}"
