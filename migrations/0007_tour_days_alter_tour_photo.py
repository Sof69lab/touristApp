# Generated by Django 4.1 on 2024-01-18 08:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("touristapp", "0006_tour_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="tour",
            name="days",
            field=models.FloatField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="tour",
            name="photo",
            field=models.ImageField(blank=True, upload_to="images"),
        ),
    ]
