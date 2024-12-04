from django.contrib import admin
from .models import Body, Lens, Accessory
from datas.models import BodyUrl, AccessoryUrl, LenseUrl
from files.models import (
    BodyFile,
    BodyPicture,
    AccessoryFile,
    AccessoryPicture,
    LensFile,
    LensPicture,
)
from django.utils.html import mark_safe
from django.db import models
from django.forms import Textarea, TextInput
from camgear.common import CommonAdmin
from camgear.utils import AdminImageWidget
from repairlog.models import BodyRepairLog, LensRepairLog, AccessoryRepairLog


class BodyUrlsInline(admin.TabularInline):
    model = BodyUrl
    extra = 0
    verbose_name = "URL"
    verbose_name_plural = "URLs"
    formfield_overrides = {
        models.URLField: {"widget": TextInput(attrs={"size": 80})},
    }


class AccessoryUrlsInline(admin.TabularInline):
    model = AccessoryUrl
    extra = 0
    verbose_name = "URL"
    verbose_name_plural = "URLs"
    formfield_overrides = {
        models.URLField: {"widget": TextInput(attrs={"size": 80})},
    }


class LensUrlsInline(admin.TabularInline):
    model = LenseUrl
    extra = 0
    verbose_name = "URL"
    verbose_name_plural = "URLs"
    formfield_overrides = {
        models.URLField: {"widget": TextInput(attrs={"size": 80})},
    }


class BodyPicturesInline(admin.TabularInline):
    model = BodyPicture
    extra = 0
    verbose_name = "Picture"
    verbose_name_plural = "Pictures"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
        models.ImageField: {"widget": AdminImageWidget},
    }


class BodyFilesInline(admin.TabularInline):
    model = BodyFile
    extra = 0
    verbose_name = "File"
    verbose_name_plural = "Files"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
    }


class LensPicturesInline(admin.TabularInline):
    model = LensPicture
    extra = 0
    verbose_name = "Picture"
    verbose_name_plural = "Pictures"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
        models.ImageField: {"widget": AdminImageWidget},
    }


class LensFilesInline(admin.TabularInline):
    model = LensFile
    extra = 0
    verbose_name = "File"
    verbose_name_plural = "Files"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
    }


class AccessoryPicturesInline(admin.TabularInline):
    model = AccessoryPicture
    extra = 0
    verbose_name = "Picture"
    verbose_name_plural = "Pictures"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
        models.ImageField: {"widget": AdminImageWidget},
    }


class AccessoryFilesInline(admin.TabularInline):
    model = AccessoryFile
    extra = 0
    verbose_name = "File"
    verbose_name_plural = "Files"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
    }


class BodyRepairLogInline(admin.TabularInline):
    model = BodyRepairLog
    extra = 0
    verbose_name = "Repair Log"
    verbose_name_plural = "Repair Logs"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
    }


class LensRepairLogInline(admin.TabularInline):
    model = LensRepairLog
    extra = 0
    verbose_name = "Repair Log"
    verbose_name_plural = "Repair Logs"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
    }


class AccessoryRepairLogInline(admin.TabularInline):
    model = AccessoryRepairLog
    extra = 0
    verbose_name = "Repair Log"
    verbose_name_plural = "Repair Logs"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
    }


class BodyAdmin(CommonAdmin):
    list_display = (
        # "id",
        "camera_model",
        "picture",
        "state",
        "system",
        "camera_focale",
        "camera_aperture",
        "focus",
        "details",
    )

    search_fields = ("name", "state_notes", "model_notes", "description", "serial")

    def details(self, obj):
        x = []
        if obj.state_notes:
            x.append(f"<small>State: {obj.state_notes}</small>")
        if obj.model_notes:
            x.append(f"<small>Notes: {obj.model_notes}</small>")
        if obj.description:
            x.append(f"<small>Description: {obj.description}</small>")
        return mark_safe("<br>".join(x))

    def picture(self, obj):
        if obj.body_pictures and obj.body_pictures.first():
            return mark_safe(
                "<a href='{url_full}' title='Show picture in new tab' target='_blank'><img src='{url_img}'/></a>".format(
                    url_img=obj.body_pictures.first().file_small.url,
                    url_full=obj.body_pictures.first().file.url,
                )
            )
        else:
            return None

    def camera_model(self, obj):
        return obj.__str__()

    def camera_focale(self, obj):
        if obj.fixed_lens:
            return f"{obj.focale_min or 'x'} - {obj.focale_max or 'x'}"
        else:
            return "-"

    def camera_aperture(self, obj):
        if obj.fixed_lens:
            return f"{obj.min_aperture or 'x'} - {obj.max_aperture or 'x'}"
        else:
            return "-"

    list_filter = ("manufacturer", "system", "film_type", "can_be_sold")

    inlines = [BodyUrlsInline, BodyPicturesInline, BodyFilesInline, BodyRepairLogInline]

    autocomplete_fields = (
        "manufacturer",
        "system",
    )

    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 10, "cols": 100})},
        models.CharField: {"widget": TextInput(attrs={"size": 40})},
        models.URLField: {"widget": TextInput(attrs={"size": 80})},
    }

    readonly_fields = ["uuid"]

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    (
                        "manufacturer",
                        "model",
                        "serial",
                    ),
                    (
                        "state",
                        "model_notes",
                    ),
                    (
                        "state_notes",
                        "description",
                    ),
                    ("acquired_on", "acquired_for", "acquired_note"),
                    ("camera_type", "film_type", "system"),
                    ("batteries"),
                    ("iso_min", "iso_max"),
                    ("focale_min", "focale_max"),
                    ("min_aperture", "max_aperture"),
                    (
                        "shutter",
                        "auto_expo",
                        "hot_shoe",
                        "fixed_lens",
                        "macro",
                        "auto_focus",
                    ),
                    ("filter_diameter", "weight", "length"),
                    ("focus", "macro_length", "focus_length"),
                    ("private", "can_be_sold"),
                    ("uuid",),
                ),
                "classes": (
                    "baton-tabs-init",
                    "baton-tab-group-fs-p",
                ),
            },
        ),
    )

    exclude = [
        "user",
    ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)


class LensAdmin(CommonAdmin):
    list_display = (
        # "id",
        "lens_model",
        "picture",
        "state",
        "system",
        "lens_focale",
        "lens_aperture",
        "filter_diameter",
        "focus",
        "details",
    )

    search_fields = ("name", "state_notes", "model_notes", "description", "serial")

    def details(self, obj):
        x = []
        if obj.state_notes:
            x.append(f"<small>State: {obj.state_notes}</small>")
        if obj.model_notes:
            x.append(f"<small>Notes: {obj.model_notes}</small>")
        if obj.description:
            x.append(f"<small>Description: {obj.description}</small>")
        return mark_safe("<br>".join(x))

    def lens_model(self, obj):
        return obj.__str__()

    def lens_focale(self, obj):
        return f"{obj.focale_min or 'x'} - {obj.focale_max or 'x'}"

    def picture(self, obj):
        if obj.lens_pictures and obj.lens_pictures.first():
            return mark_safe(
                "<a href='{url_full}' title='Show picture in new tab' target='_blank'><img src='{url_img}'/></a>".format(
                    url_img=obj.lens_pictures.first().file_small.url,
                    url_full=obj.lens_pictures.first().file.url,
                )
            )
        else:
            return None

    def lens_aperture(self, obj):
        return f"{obj.min_aperture or 'x'} - {obj.max_aperture or 'x'}"

    list_filter = ("manufacturer", "system", "lens_type", "can_be_sold")

    inlines = [LensUrlsInline, LensPicturesInline, LensFilesInline, LensRepairLogInline]

    autocomplete_fields = (
        "manufacturer",
        "system",
    )

    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 10, "cols": 100})},
        models.CharField: {"widget": TextInput(attrs={"size": 40})},
        models.URLField: {"widget": TextInput(attrs={"size": 80})},
    }

    readonly_fields = ["uuid"]

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    (
                        "manufacturer",
                        "model",
                        "serial",
                    ),
                    (
                        "state",
                        "model_notes",
                    ),
                    (
                        "state_notes",
                        "description",
                    ),
                    ("acquired_on", "acquired_for", "acquired_note"),
                    ("lens_type", "system"),
                    ("focale_min", "focale_max"),
                    ("min_aperture", "max_aperture"),
                    ("blades"),
                    ("filter_diameter", "weight", "length"),
                    ("focus", "focus_length", "macro", "macro_length"),
                    ("private", "can_be_sold"),
                    ("uuid",),
                ),
                "classes": (
                    "baton-tabs-init",
                    "baton-tab-group-fs-p",
                ),
            },
        ),
    )

    exclude = [
        "user",
    ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)


class AccessoryAdmin(CommonAdmin):
    list_display = (
        # "id",
        "accessory_model",
        "picture",
        "state",
        "system",
        "details",
    )

    search_fields = ("name", "state_notes", "model_notes", "description", "serial")

    def accessory_model(self, obj):
        return obj.__str__()

    def picture(self, obj):
        if obj.accessory_pictures and obj.accessory_pictures.first():
            return mark_safe(
                "<a href='{url_full}' title='Show picture in new tab' target='_blank'><img src='{url_img}'/></a>".format(
                    url_img=obj.accessory_pictures.first().file_small.url,
                    url_full=obj.accessory_pictures.first().file.url,
                )
            )
        else:
            return None

    def details(self, obj):
        x = []
        if obj.state_notes:
            x.append(f"<small>State: {obj.state_notes}</small>")
        if obj.model_notes:
            x.append(f"<small>Notes: {obj.model_notes}</small>")
        if obj.description:
            x.append(f"<small>Description: {obj.description}</small>")
        return mark_safe("<br>".join(x))

    list_filter = ("manufacturer", "system", "can_be_sold")

    inlines = [
        AccessoryUrlsInline,
        AccessoryPicturesInline,
        AccessoryFilesInline,
        AccessoryRepairLogInline,
    ]

    autocomplete_fields = (
        "manufacturer",
        "system",
    )

    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 10, "cols": 100})},
        models.CharField: {"widget": TextInput(attrs={"size": 40})},
        models.URLField: {"widget": TextInput(attrs={"size": 80})},
    }

    readonly_fields = ["uuid"]

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    (
                        "manufacturer",
                        "model",
                        "serial",
                    ),
                    (
                        "state",
                        "model_notes",
                    ),
                    (
                        "state_notes",
                        "description",
                    ),
                    ("acquired_on", "acquired_for", "acquired_note"),
                    ("batteries", "system"),
                    ("private", "can_be_sold"),
                    ("uuid",),
                ),
                "classes": (
                    "baton-tabs-init",
                    "baton-tab-group-fs-p",
                ),
            },
        ),
    )

    exclude = [
        "user",
    ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Body, BodyAdmin)
admin.site.register(Lens, LensAdmin)
admin.site.register(Accessory, AccessoryAdmin)
