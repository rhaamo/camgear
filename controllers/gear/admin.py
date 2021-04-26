from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from config.admin import CommonAdmin
from django.utils.html import mark_safe

from .models import Camera, Manufacturer, Mount, Lens

from controllers.files.models import CameraPicture, LensPicture, CameraFile, LensFile


class CameraPicturesInline(admin.TabularInline):
    model = CameraPicture
    extra = 0
    verbose_name = "Picture"
    verbose_name_plural = "Pictures"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
    }


class CameraFilesInline(admin.TabularInline):
    model = CameraFile
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
    }


class LensFilesInline(admin.TabularInline):
    model = LensFile
    extra = 0
    verbose_name = "File"
    verbose_name_plural = "Files"
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": 80})},
    }


class CameraAdmin(CommonAdmin):
    list_display = (
        "id",
        "picture",
        "camera_model",
        "state",
        "mount",
        "camera_focale",
        "camera_aperture",
        "focus",
    )

    search_fields = ("name", "state_notes", "model_notes", "description")

    def picture(self, obj):
        if obj.camera_pictures and obj.camera_pictures.first():
            return mark_safe(
                "<a href='{url_img}' target='_blank'><img src='{url_img}'/></a>".format(
                    url_img=obj.camera_pictures.first().file_mini.url
                )
            )
        else:
            return None

    def camera_model(self, obj):
        return obj.__str__()

    def camera_focale(self, obj):
        return f"{obj.focale_min or 'x'} - {obj.focale_max or 'x'}"

    def camera_aperture(self, obj):
        return f"{obj.min_aperture or 'x'} - {obj.max_aperture or 'x'}"

    list_filter = ("manufacturer", "mount", "film_type")

    inlines = [CameraPicturesInline, CameraFilesInline]

    autocomplete_fields = (
        "manufacturer",
        "mount",
    )

    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 10, "cols": 100})},
        models.CharField: {"widget": TextInput(attrs={"size": 40})},
        models.URLField: {"widget": TextInput(attrs={"size": 80})},
    }

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
                        "state_notes",
                        "model_notes",
                    ),
                    "description",
                    ("camera_type", "film_type", "mount"),
                    ("batteries", "hot_shoe", "fixed_lens"),
                    ("iso_min", "iso_max"),
                    ("focale_min", "focale_max"),
                    ("min_aperture", "max_aperture"),
                    ("blades"),
                    ("filter_diameter", "weight", "length"),
                    ("focus", "macro", "macro_length"),
                    ("private", "can_be_sold"),
                ),
                "classes": (
                    "baton-tabs-init",
                    "baton-tab-group-fs-p",
                ),
            },
        ),
        (
            "Links",
            {
                "fields": ("url1", "url2", "url3"),
                "classes": ("tab-fs-p",),
            },
        ),
    )


class ManufacturerAdmin(CommonAdmin):
    search_fields = ("name",)


class MountAdmin(CommonAdmin):
    search_fields = ("name",)


class LensAdmin(CommonAdmin):
    list_display = (
        "id",
        "picture",
        "lens_model",
        "state",
        "mount",
        "lens_focale",
        "lens_aperture",
        "focus",
    )

    search_fields = ("name", "state_notes", "model_notes", "description")

    def lens_model(self, obj):
        return obj.__str__()

    def lens_focale(self, obj):
        return f"{obj.focale_min or 'x'} - {obj.focale_max or 'x'}"

    def picture(self, obj):
        if obj.lens_pictures and obj.lens_pictures.first():
            return mark_safe(
                "<a href='{url_img}' target='_blank'><img src='{url_img}'/></a>".format(
                    url_img=obj.lens_pictures.first().file_mini.url
                )
            )
        else:
            return None

    def lens_aperture(self, obj):
        return f"{obj.min_aperture or 'x'} - {obj.max_aperture or 'x'}"

    list_filter = ("manufacturer", "mount", "lens_type")

    inlines = [LensPicturesInline, LensFilesInline]

    autocomplete_fields = (
        "manufacturer",
        "mount",
    )

    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 10, "cols": 100})},
        models.CharField: {"widget": TextInput(attrs={"size": 40})},
        models.URLField: {"widget": TextInput(attrs={"size": 80})},
    }

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
                        "state_notes",
                        "model_notes",
                    ),
                    "description",
                    ("lens_type", "mount"),
                    ("focale_min", "focale_max"),
                    ("min_aperture", "max_aperture"),
                    ("blades", "angle"),
                    ("filter_diameter", "weight", "length"),
                    ("focus", "focus_length", "macro", "macro_length"),
                    ("private", "can_be_sold"),
                ),
                "classes": (
                    "baton-tabs-init",
                    "baton-tab-group-fs-p",
                ),
            },
        ),
        (
            "Links",
            {
                "fields": ("url1", "url2", "url3"),
                "classes": ("tab-fs-p",),
            },
        ),
    )


admin.site.register(Camera, CameraAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Mount, MountAdmin)
admin.site.register(Lens, LensAdmin)
