from django.db import models
from django.conf import settings
from .enums import (
    States,
    CamerasTypes,
    FilmTypes,
    FocusesTypes,
    LensesTypes,
    ShutterTypes,
)
from datas.models import Manufacturer, System
import uuid


class Body(models.Model):
    state = models.IntegerField(blank=False, default=States.UNKNOWN, choices=States.choices)
    state_notes = models.TextField(blank=True)
    wip_sheet = models.BooleanField(help_text="Is this sheet still a WIP ?", default=True)

    system = models.ForeignKey(System, blank=True, null=True, on_delete=models.SET_NULL)
    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL)
    model = models.CharField(max_length=255, blank=True)
    model_notes = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    serial = models.CharField("Serial (private)", max_length=255, blank=True)

    camera_type = models.IntegerField(blank=False, default=CamerasTypes.UNKNOWN, choices=CamerasTypes.choices)
    film_type = models.IntegerField(blank=False, default=FilmTypes.UNKNOWN, choices=FilmTypes.choices)

    auto_expo = models.BooleanField("Auto Exposure", default=False)
    auto_focus = models.BooleanField("Auto Focus", default=False)
    batteries = models.CharField(max_length=255, blank=True)  # TODO: autocomplete
    hot_shoe = models.BooleanField(default=True)
    fixed_lens = models.BooleanField(default=False)

    iso_min = models.IntegerField("ISO min", default=0)
    iso_max = models.IntegerField("ISO max", default=0)
    iso_dx = models.BooleanField("ISO DX Auto", default=False)
    focale_min = models.IntegerField("Focale min (mm)", blank=False, default=0)
    focale_max = models.IntegerField("Focale max (mm)", blank=False, default=0)
    min_aperture = models.FloatField(default=0)
    max_aperture = models.FloatField(default=0)
    shutter = models.IntegerField(
        "Shutter type",
        blank=False,
        default=ShutterTypes.UNKNOWN,
        choices=ShutterTypes.choices,
    )
    filter_diameter = models.IntegerField("Filter Dia. (mm)", default=0)
    weight = models.IntegerField("Weight (g)", default=0)  # g.
    length = models.IntegerField("Length (cm)", default=0)  # cm
    focus = models.IntegerField(
        "Focus mode",
        blank=False,
        default=FocusesTypes.UNKNOWN,
        choices=FocusesTypes.choices,
    )
    focus_length = models.IntegerField("Min focus (cm)", default=0)
    macro = models.BooleanField("Macro capable", default=True)
    macro_length = models.IntegerField("Min macro (cm)", default=0)

    private = models.BooleanField(default=False)
    can_be_sold = models.BooleanField(default=False)

    acquired_on = models.DateField(blank=True, null=True)
    acquired_for = models.IntegerField(blank=False, default=0)
    acquired_note = models.CharField(max_length=255, blank=True)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Bodies"

    def features_str(self):
        _features = []
        if self.auto_expo:
            _features.append("Auto exposure")
        if self.hot_shoe:
            _features.append("Hot-shoe")
        if self.fixed_lens:
            _features.append("Fixed lens")
        if self.macro:
            _features.append("Macro capable")
        if self.auto_focus:
            _features.append("Auto focus")
        if len(_features) == 0:
            return None
        return ", ".join(_features)

    def iso_str(self):
        if not self.iso_min and not self.iso_max:
            return None
        if self.iso_min == self.iso_max:
            return self.iso_min
        if self.iso_min != self.iso_max:
            return f"{self.iso_min} - {self.iso_max}"

    def focale_str(self):
        if not self.focale_min and not self.focale_max:
            return None
        if self.focale_min == self.focale_max:
            return self.focale_min
        if self.focale_min != self.focale_max:
            return f"{self.focale_min} - {self.focale_max}"

    def aperture_str(self):
        if not self.min_aperture and not self.max_aperture:
            return None
        if self.min_aperture == self.max_aperture:
            return self.min_aperture
        if self.min_aperture != self.max_aperture:
            return f"{self.min_aperture} - {self.max_aperture}"

    def __str__(self):
        name = []
        if self.manufacturer:
            name.append(self.manufacturer.name)
        if self.model:
            name.append(self.model)
        return " ".join(name)


class Lens(models.Model):
    state = models.IntegerField(blank=False, default=States.UNKNOWN, choices=States.choices)
    state_notes = models.TextField(blank=True)
    wip_sheet = models.BooleanField(help_text="Is this sheet still a WIP ?", default=True)

    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL)
    model = models.CharField(max_length=255, blank=True)
    model_notes = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    serial = models.CharField("Serial (private)", max_length=255, blank=True)
    system = models.ForeignKey(System, blank=True, null=True, on_delete=models.SET_NULL)

    focale_min = models.IntegerField("Focale min (mm)", blank=False, default=0)
    focale_max = models.IntegerField("Focale max (mm)", blank=False, default=0)
    min_aperture = models.FloatField(help_text="ex 22", default=0)
    max_aperture = models.FloatField(help_text="ex 2.8", default=0)
    lens_type = models.IntegerField(blank=False, default=LensesTypes.UNKNOWN, choices=LensesTypes.choices)
    macro = models.BooleanField("Macro capable", default=True)
    macro_length = models.IntegerField("Min macro (cm)", default=0)
    filter_diameter = models.IntegerField("Filter Dia. (mm)", default=0)
    blades = models.BooleanField("Using blades", default=True)
    focus = models.IntegerField(
        "Focus mode",
        blank=False,
        default=FocusesTypes.UNKNOWN,
        choices=FocusesTypes.choices,
    )
    focus_length = models.IntegerField("Min focus (cm)", default=0)
    weight = models.IntegerField("Weight (g)", default=0)  # g.
    length = models.FloatField("Length (cm)", default=0)  # cm

    private = models.BooleanField(default=False)
    can_be_sold = models.BooleanField(default=False)

    acquired_on = models.DateField(blank=True, null=True)
    acquired_for = models.IntegerField(blank=False, default=0)
    acquired_note = models.CharField(max_length=255, blank=True)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Lenses"

    def features_str(self):
        _features = []
        if self.blades:
            _features.append("Has blades")
        if len(_features) == 0:
            return None
        return ", ".join(_features)

    def focale_str(self):
        if not self.focale_min and not self.focale_max:
            return None
        if self.focale_min == self.focale_max:
            return self.focale_min
        if self.focale_min != self.focale_max:
            return f"{self.focale_min} - {self.focale_max}"

    def aperture_str(self):
        if not self.min_aperture and not self.max_aperture:
            return None
        if self.min_aperture == self.max_aperture:
            return self.min_aperture
        if self.min_aperture != self.max_aperture:
            return f"{self.min_aperture} - {self.max_aperture}"

    def __str__(self):
        name = []
        if self.manufacturer:
            name.append(self.manufacturer.name)
        if self.model:
            name.append(self.model)
        return " ".join(name)


class Accessory(models.Model):
    state = models.IntegerField(blank=False, default=States.UNKNOWN, choices=States.choices)
    state_notes = models.TextField(blank=True)
    wip_sheet = models.BooleanField(help_text="Is this sheet still a WIP ?", default=True)

    manufacturer = models.ForeignKey(Manufacturer, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, null=True)
    model = models.CharField(max_length=255, blank=True)
    model_notes = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    serial = models.CharField("Serial (private)", max_length=255, blank=True)
    system = models.ForeignKey(System, blank=True, null=True, on_delete=models.SET_NULL)
    batteries = models.CharField(max_length=255, blank=True)  # autocomplete

    private = models.BooleanField(default=False)
    can_be_sold = models.BooleanField(default=False)

    acquired_on = models.DateField(blank=True, null=True)
    acquired_for = models.IntegerField(blank=False, default=0)
    acquired_note = models.CharField(max_length=255, blank=True)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = "Accessories"

    def __str__(self):
        name = []
        if self.manufacturer:
            name.append(self.manufacturer.name)
        if self.model:
            name.append(self.model)
        return " ".join(name)
