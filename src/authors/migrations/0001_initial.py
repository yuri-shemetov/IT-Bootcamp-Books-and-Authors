# Generated by Django 4.2.3 on 2023-07-31 10:17

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.IntegerField(verbose_name="Количество авторов")),
                ("name", models.CharField(max_length=30, verbose_name="Автор(ы)")),
                (
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата внесения в БД"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата последнего редактирования"
                    ),
                ),
            ],
            options={
                "verbose_name": "Автора",
                "verbose_name_plural": "Авторы",
            },
        ),
    ]
