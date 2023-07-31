from django.db import models
from django.urls import reverse

from authors.models import Author


class Book(models.Model):
    picture = models.ImageField(
        "Картинка",
        upload_to="books/%Y/%m/%d",
    )

    name = models.CharField(
        max_length=40,
        verbose_name="Название книги",
    )

    price = models.FloatField(
        verbose_name="Цена",
    )

    author = models.ManyToManyField(
        Author,
        related_name="Author",
        verbose_name="Автор",
    )

    year = models.IntegerField(
        verbose_name="Год издания",
    )

    pages = models.IntegerField(
        verbose_name="Страниц",
    )

    quantity = models.IntegerField(
        verbose_name="Количество книг",
    )

    avtive = models.BooleanField(
        verbose_name="Активный",
        default=False,
    )

    created = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now=False,
        auto_now_add=True,
    )

    updated = models.DateTimeField(
        verbose_name="Дата последнего редактирования",
        auto_now=True,
        auto_now_add=False,
    )

    def __str__(self) -> str:
        return f"{self.name} - {self.author.all()}"

    def get_absolute_url(self):
        return reverse("books")

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
