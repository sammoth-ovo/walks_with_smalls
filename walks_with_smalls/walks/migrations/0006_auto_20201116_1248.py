# Generated by Django 3.1.3 on 2020-11-16 12:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("walks", "0005_auto_20201113_2037"),
    ]

    operations = [
        migrations.CreateModel(
            name="PostCode",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("postcode", models.CharField(max_length=100)),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name="place",
            name="reverse_geocode_cache_time",
            field=models.DateTimeField(
                default=datetime.datetime(2018, 11, 27, 12, 48, 6, 491369, tzinfo=utc)
            ),
        ),
    ]