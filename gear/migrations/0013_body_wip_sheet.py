# Generated by Django 5.1.3 on 2024-12-04 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gear", "0012_set_unique_uuids"),
    ]

    operations = [
        migrations.AddField(
            model_name="body",
            name="wip_sheet",
            field=models.BooleanField(default=True, help_text="Is this sheet still a WIP ?"),
        ),
    ]
