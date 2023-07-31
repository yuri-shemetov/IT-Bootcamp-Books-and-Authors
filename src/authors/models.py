from django.db import models
from django.urls import reverse


class Author(models.Model):
    number = models.IntegerField(
        verbose_name="Количество авторов",
    )
    name = models.CharField(max_length=30, verbose_name="Автор(ы)")
    created = models.DateTimeField(
        verbose_name="Дата внесения в БД", auto_now=False, auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name="Дата последнего редактирования", auto_now=True, auto_now_add=False
    )

    def __str__(self) -> str:
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("authors")

    class Meta:
        verbose_name = "Автора"
        verbose_name_plural = "Авторы"
