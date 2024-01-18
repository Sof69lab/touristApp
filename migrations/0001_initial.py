# Generated by Django 4.1 on 2023-11-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tour",
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
                ("name", models.TextField()),
                ("route", models.TextField()),
                ("describe", models.TextField()),
                ("transport", models.TextField()),
                ("price", models.FloatField()),
            ],
        ),
    ]
