# Generated by Django 5.1.3 on 2024-12-03 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gear", "0006_body_acquired_note"),
    ]

    operations = [
        migrations.AlterField(
            model_name="body",
            name="acquired_on",
            field=models.DateTimeField(blank=True),
        ),
    ]
