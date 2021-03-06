# Generated by Django 3.1.4 on 2021-04-26 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Manufacturer",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Mount",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Camera",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
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
                ("serial", models.CharField(blank=True, max_length=255)),
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
                ("auto_expo", models.BooleanField(default=True)),
                ("auto_focus", models.BooleanField(default=True)),
                ("batteries", models.CharField(blank=True, max_length=255)),
                ("hot_shoe", models.BooleanField(default=True)),
                ("fixed_lens", models.BooleanField(default=False)),
                ("iso_min", models.IntegerField(default=0)),
                ("iso_max", models.IntegerField(default=0)),
                ("focale_min", models.IntegerField(default=0)),
                ("focale_max", models.IntegerField(default=0)),
                ("min_aperture", models.FloatField(default=0)),
                ("max_aperture", models.FloatField(default=0)),
                ("blades", models.BooleanField(default=True)),
                ("filter_diameter", models.IntegerField(default=0)),
                ("weight", models.IntegerField(default=0)),
                ("length", models.IntegerField(default=0)),
                (
                    "focus",
                    models.IntegerField(
                        choices=[(0, "Unknown"), (5, "Manual"), (10, "Automatic"), (15, "Fixed"), (20, "Auto/Man")],
                        default=0,
                    ),
                ),
                ("macro", models.BooleanField(default=True)),
                ("macro_length", models.IntegerField(default=0)),
                ("private", models.BooleanField(default=False)),
                ("can_be_sold", models.BooleanField(default=False)),
                ("url1", models.URLField(blank=True)),
                ("url2", models.URLField(blank=True)),
                ("url3", models.URLField(blank=True)),
                (
                    "manufacturer",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="gear.manufacturer"),
                ),
                ("mount", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="gear.mount")),
            ],
        ),
    ]
