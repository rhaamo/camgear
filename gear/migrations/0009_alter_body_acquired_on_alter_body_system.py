# Generated by Django 5.1.3 on 2024-12-03 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datas", "0003_accessoryurl_private_bodyurl_private_and_more"),
        ("gear", "0008_alter_body_acquired_on"),
    ]

    operations = [
        migrations.AlterField(
            model_name="body",
            name="acquired_on",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="body",
            name="system",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="datas.system",
            ),
        ),
    ]