# Generated by Django 5.1.3 on 2024-12-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gear", "0002_alter_lens_length_alter_lens_max_aperture_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="accessory",
            name="model_notes",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="body",
            name="model_notes",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="lens",
            name="model_notes",
            field=models.TextField(blank=True),
        ),
    ]
