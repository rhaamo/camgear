# Generated by Django 5.1.3 on 2024-12-04 08:48

from django.db import migrations
import uuid


def gen_uuid_body(apps, schema_editor):
    Body = apps.get_model("gear", "Body")
    for row in Body.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=["uuid"])


def gen_uuid_lens(apps, schema_editor):
    Lens = apps.get_model("gear", "Lens")
    for row in Lens.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=["uuid"])


def gen_uuid_accessory(apps, schema_editor):
    Accessory = apps.get_model("gear", "Accessory")
    for row in Accessory.objects.all():
        row.uuid = uuid.uuid4()
        row.save(update_fields=["uuid"])


class Migration(migrations.Migration):

    dependencies = [
        ("gear", "0011_accessory_uuid_body_uuid_lens_uuid"),
    ]

    operations = [
        migrations.RunPython(gen_uuid_body),
        migrations.RunPython(gen_uuid_lens),
        migrations.RunPython(gen_uuid_accessory),
    ]
