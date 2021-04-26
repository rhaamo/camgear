from django.db import models

from .enums import States, CamerasTypes, FilmTypes, FocusesTypes, LensesTypes


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Mount(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Lens(models.Model):
    state = models.IntegerField(blank=False, default=States.UNKNOWN, choices=States.choices)
    state_notes = models.CharField(max_length=255, blank=True)

    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL)
    model = models.CharField(max_length=255, blank=True)
    model_notes = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    serial = models.CharField(max_length=255, blank=True)
    mount = models.ForeignKey(Mount, null=True, on_delete=models.SET_NULL)

    focale_min = models.IntegerField(blank=False, default=0)
    focale_max = models.IntegerField(blank=False, default=0)
    min_aperture = models.FloatField(default=0)
    max_aperture = models.FloatField(default=0)
    lens_type = models.IntegerField(blank=False, default=LensesTypes.UNKNOWN, choices=LensesTypes.choices)
    macro = models.BooleanField(default=True)
    macro_length = models.IntegerField(default=0)
    filter_diameter = models.IntegerField(default=0)
    blades = models.BooleanField(default=True)
    angle = models.FloatField(default=0, blank=True)
    focus = models.IntegerField(blank=False, default=FocusesTypes.UNKNOWN, choices=FocusesTypes.choices)
    focus_length = models.IntegerField(default=0, blank=True)
    weight = models.IntegerField(default=0)  # g.
    length = models.IntegerField(default=0)  # mm

    private = models.BooleanField(default=False)
    can_be_sold = models.BooleanField(default=False)

    url1 = models.URLField(blank=True)
    url2 = models.URLField(blank=True)
    url3 = models.URLField(blank=True)

    # TODO pictures
    # TODO documents

    # TODO user

    class Meta:
        verbose_name_plural = "Lenses"

    def __str__(self):
        name = []
        if self.manufacturer:
            name.append(self.manufacturer.name)
        if self.model:
            name.append(self.model)
        return " ".join(name)


class Camera(models.Model):
    state = models.IntegerField(blank=False, default=States.UNKNOWN, choices=States.choices)
    state_notes = models.CharField(max_length=255, blank=True)

    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL)
    model = models.CharField(max_length=255, blank=True)
    model_notes = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    serial = models.CharField(max_length=255, blank=True)
    mount = models.ForeignKey(Mount, null=True, on_delete=models.SET_NULL)

    camera_type = models.IntegerField(blank=False, default=CamerasTypes.UNKNOWN, choices=CamerasTypes.choices)

    film_type = models.IntegerField(blank=False, default=FilmTypes.UNKNOWN, choices=FilmTypes.choices)
    auto_expo = models.BooleanField(default=True)
    auto_focus = models.BooleanField(default=True)
    batteries = models.CharField(max_length=255, blank=True)  # autocomplete
    hot_shoe = models.BooleanField(default=True)
    fixed_lens = models.BooleanField(default=False)

    iso_min = models.IntegerField(default=0)
    iso_max = models.IntegerField(default=0)
    focale_min = models.IntegerField(blank=False, default=0)
    focale_max = models.IntegerField(blank=False, default=0)
    min_aperture = models.FloatField(default=0)
    max_aperture = models.FloatField(default=0)
    blades = models.BooleanField(default=True)
    filter_diameter = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)  # g.
    length = models.IntegerField(default=0)  # mm
    focus = models.IntegerField(blank=False, default=FocusesTypes.UNKNOWN, choices=FocusesTypes.choices)
    macro = models.BooleanField(default=True)
    macro_length = models.IntegerField(default=0)

    private = models.BooleanField(default=False)
    can_be_sold = models.BooleanField(default=False)

    url1 = models.URLField(blank=True)
    url2 = models.URLField(blank=True)
    url3 = models.URLField(blank=True)

    # TODO pictures
    # TODO documents

    # TODO user

    def __str__(self):
        name = []
        if self.manufacturer:
            name.append(self.manufacturer.name)
        if self.model:
            name.append(self.model)
        return " ".join(name)
