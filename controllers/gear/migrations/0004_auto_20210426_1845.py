# Generated by Django 3.1.8 on 2021-04-26 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gear", "0003_auto_20210426_1813"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="camera",
            name="files",
        ),
        migrations.RemoveField(
            model_name="camera",
            name="pictures",
        ),
        migrations.RemoveField(
            model_name="lens",
            name="files",
        ),
        migrations.RemoveField(
            model_name="lens",
            name="pictures",
        ),
    ]