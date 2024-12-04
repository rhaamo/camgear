# Generated by Django 5.1.3 on 2024-12-04 08:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gear", "0010_accessory_acquired_for_accessory_acquired_note_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="accessory",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name="body",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddField(
            model_name="lens",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
