# Generated by Django 5.1.3 on 2024-12-04 11:05

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gear", "0013_body_wip_sheet"),
        ("repairlog", "0003_remove_bodyrepairlog_user"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bodyrepairlog",
            options={"ordering": ("-done_at",), "verbose_name_plural": "Repair Logs"},
        ),
        migrations.AlterField(
            model_name="bodyrepairlog",
            name="done_at",
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.CreateModel(
            name="AccessoryRepairLog",
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
                ("title", models.CharField(default="Repair log", max_length=255)),
                ("note", models.TextField()),
                ("done_at", models.DateTimeField(default=datetime.datetime.now)),
                ("private", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "body",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="Accessory_repairlog",
                        to="gear.accessory",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Repair Logs",
                "ordering": ("-done_at",),
            },
        ),
        migrations.CreateModel(
            name="LensRepairLog",
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
                ("title", models.CharField(default="Repair log", max_length=255)),
                ("note", models.TextField()),
                ("done_at", models.DateTimeField(default=datetime.datetime.now)),
                ("private", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "body",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="lens_repairlog",
                        to="gear.lens",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Repair Logs",
                "ordering": ("-done_at",),
            },
        ),
    ]
