# Generated by Django 4.1 on 2024-01-17 12:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("touristapp", "0004_alter_reservation_name_alter_reservation_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="reservation",
            name="cost",
            field=models.FloatField(default=750),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="reservation",
            name="people",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
