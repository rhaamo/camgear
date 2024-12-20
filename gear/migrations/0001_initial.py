# Generated by Django 5.1.3 on 2024-12-03 16:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("datas", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Accessory",
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
                (
                    "state",
                    models.IntegerField(
                        choices=[
                            (0, "Unknown"),
                            (5, "Very Good"),
                            (10, "Good"),
                            (15, "Ok, scratches"),
                            (20, "Not so ok"),
                            (25, "Cracks"),
                            (30, "Partly working"),
                            (35, "Not working"),
                            (40, "Lost"),
                            (45, "Stolen"),
                        ],
                        default=0,
                    ),
                ),
                ("state_notes", models.CharField(blank=True, max_length=255)),
                ("name", models.CharField(max_length=255, null=True)),
                ("model", models.CharField(blank=True, max_length=255)),
                ("model_notes", models.CharField(blank=True, max_length=255)),
                ("description", models.TextField(blank=True)),
                (
                    "serial",
                    models.CharField(blank=True, max_length=255, verbose_name="Serial (private)"),
                ),
                ("batteries", models.CharField(blank=True, max_length=255)),
                ("private", models.BooleanField(default=False)),
                ("can_be_sold", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="datas.manufacturer",
                    ),
                ),
                (
                    "system",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="datas.system",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Accessories",
            },
        ),
        migrations.CreateModel(
            name="Body",
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
                (
                    "state",
                    models.IntegerField(
                        choices=[
                            (0, "Unknown"),
                            (5, "Very Good"),
                            (10, "Good"),
                            (15, "Ok, scratches"),
                            (20, "Not so ok"),
                            (25, "Cracks"),
                            (30, "Partly working"),
                            (35, "Not working"),
                            (40, "Lost"),
                            (45, "Stolen"),
                        ],
                        default=0,
                    ),
                ),
                ("state_notes", models.CharField(blank=True, max_length=255)),
                ("model", models.CharField(blank=True, max_length=255)),
                ("model_notes", models.CharField(blank=True, max_length=255)),
                ("description", models.TextField(blank=True)),
                (
                    "serial",
                    models.CharField(blank=True, max_length=255, verbose_name="Serial (private)"),
                ),
                (
                    "camera_type",
                    models.IntegerField(
                        choices=[
                            (0, "Unknown"),
                            (5, "Chamber"),
                            (10, "Chamber Stereo"),
                            (15, "Folding"),
                            (20, "Box"),
                            (25, "Box Stereo"),
                            (30, "Instant"),
                            (35, "Disposable"),
                            (40, "Toy"),
                            (45, "Panoramic"),
                            (50, "Reflex SLR"),
                            (55, "Reflex TLR"),
                            (60, "Reflex DSLR"),
                            (65, "Digital"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "film_type",
                    models.IntegerField(
                        choices=[
                            (0, "Unknown"),
                            (5, "8mm"),
                            (10, "9.5mm"),
                            (15, "16mm"),
                            (20, "17.5mm"),
                            (25, "28mm"),
                            (30, "35mm"),
                            (35, "70mm"),
                            (40, "110"),
                            (45, "120"),
                            (50, "126"),
                            (55, "127"),
                            (60, "135"),
                            (65, "616"),
                            (70, "628"),
                            (75, "Disc"),
                            (80, "Ektachrome"),
                            (85, "Ektar"),
                            (90, "Kodachrome"),
                            (95, "Eastmancolor"),
                            (100, "Plate"),
                            (105, "Pack-Film"),
                            (110, "Pack-Film 100"),
                            (115, "Pack-Film 100 or 80"),
                            (120, "Pack-Film 80"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "auto_expo",
                    models.BooleanField(default=False, verbose_name="Auto Exposure"),
                ),
                (
                    "auto_focus",
                    models.BooleanField(default=False, verbose_name="Auto Focus"),
                ),
                ("batteries", models.CharField(blank=True, max_length=255)),
                ("hot_shoe", models.BooleanField(default=True)),
                ("fixed_lens", models.BooleanField(default=False)),
                ("iso_min", models.IntegerField(default=0, verbose_name="ISO min")),
                ("iso_max", models.IntegerField(default=0, verbose_name="ISO max")),
                (
                    "iso_dx",
                    models.BooleanField(default=False, verbose_name="ISO DX Auto"),
                ),
                (
                    "focale_min",
                    models.IntegerField(default=0, verbose_name="Focale min (mm)"),
                ),
                (
                    "focale_max",
                    models.IntegerField(default=0, verbose_name="Focale max (mm)"),
                ),
                ("min_aperture", models.FloatField(default=0)),
                ("max_aperture", models.FloatField(default=0)),
                (
                    "shutter",
                    models.IntegerField(
                        choices=[
                            (0, "Unknown"),
                            (5, "Curtains"),
                            (10, "Blades (body)"),
                            (15, "Blades (lens)"),
                        ],
                        default=0,
                        verbose_name="Shutter type",
                    ),
                ),
                (
                    "filter_diameter",
                    models.IntegerField(default=0, verbose_name="Filter Dia. (mm)"),
                ),
                ("weight", models.IntegerField(default=0, verbose_name="Weight (g)")),
                ("length", models.IntegerField(default=0, verbose_name="Length (cm)")),
                (
                    "focus",
                    models.IntegerField(
                        choices=[
                            (0, "Unknown"),
                            (5, "Manual"),
                            (10, "Automatic"),
                            (15, "Fixed"),
                            (20, "Auto/Man"),
                        ],
                        default=0,
                        verbose_name="Focus mode",
                    ),
                ),
                (
                    "focus_length",
                    models.IntegerField(default=0, verbose_name="Min focus (cm)"),
                ),
                (
                    "macro",
                    models.BooleanField(default=True, verbose_name="Macro capable"),
                ),
                (
                    "macro_length",
                    models.IntegerField(default=0, verbose_name="Min macro (cm)"),
                ),
                ("private", models.BooleanField(default=False)),
                ("can_be_sold", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="datas.manufacturer",
                    ),
                ),
                (
                    "system",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="datas.system",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Bodies",
            },
        ),
        migrations.CreateModel(
            name="Lens",
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
                (
                    "state",
                    models.IntegerField(
                        choices=[
                            (0, "Unknown"),
                            (5, "Very Good"),
                            (10, "Good"),
                            (15, "Ok, scratches"),
                            (20, "Not so ok"),
                            (25, "Cracks"),
                            (30, "Partly working"),
                            (35, "Not working"),
                            (40, "Lost"),
                            (45, "Stolen"),
                        ],
                        default=0,
                    ),
                ),
                ("state_notes", models.CharField(blank=True, max_length=255)),
                ("model", models.CharField(blank=True, max_length=255)),
                ("model_notes", models.CharField(blank=True, max_length=255)),
                ("description", models.TextField(blank=True)),
                (
                    "serial",
                    models.CharField(blank=True, max_length=255, verbose_name="Serial (private)"),
                ),
                (
                    "focale_min",
                    models.IntegerField(default=0, verbose_name="Focale min (mm)"),
                ),
                (
                    "focale_max",
                    models.IntegerField(default=0, verbose_name="Focale max (mm)"),
                ),
                ("min_aperture", models.FloatField(default=0)),
                ("max_aperture", models.FloatField(default=0)),
                (
                    "lens_type",
                    models.IntegerField(
                        choices=[
                            (0, "Unknown"),
                            (5, "Wide Angle"),
                            (10, "Standard"),
                            (15, "Zoom"),
                            (20, "Telephoto"),
                        ],
                        default=0,
                    ),
                ),
                (
                    "macro",
                    models.BooleanField(default=True, verbose_name="Macro capable"),
                ),
                (
                    "macro_length",
                    models.IntegerField(default=0, verbose_name="Min macro (cm)"),
                ),
                (
                    "filter_diameter",
                    models.IntegerField(default=0, verbose_name="Filter Dia. (mm)"),
                ),
                (
                    "blades",
                    models.BooleanField(default=True, verbose_name="Using blades"),
                ),
                ("angle", models.FloatField(blank=True, default=0)),
                (
                    "focus",
                    models.IntegerField(
                        choices=[
                            (0, "Unknown"),
                            (5, "Manual"),
                            (10, "Automatic"),
                            (15, "Fixed"),
                            (20, "Auto/Man"),
                        ],
                        default=0,
                        verbose_name="Focus mode",
                    ),
                ),
                (
                    "focus_length",
                    models.IntegerField(default=0, verbose_name="Min focus (cm)"),
                ),
                ("weight", models.IntegerField(default=0, verbose_name="Weight (g)")),
                ("length", models.IntegerField(default=0, verbose_name="Length (cm)")),
                ("private", models.BooleanField(default=False)),
                ("can_be_sold", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "manufacturer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="datas.manufacturer",
                    ),
                ),
                (
                    "system",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="datas.system",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Lenses",
            },
        ),
    ]
