# Generated by Django 5.1.3 on 2024-12-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gear", "0004_alter_accessory_model_notes_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="body",
            name="acquired_for",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="body",
            name="acquired_on",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
