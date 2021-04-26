from django.contrib import admin
from django.db import models
from baton.admin import DropdownFilter
from imagekit.admin import AdminThumbnail
from django.forms import TextInput

from config.admin import CommonAdmin
from .models import CameraFile, CameraPicture, LensFile, LensPicture


class CameraPicturesAdmin(CommonAdmin):
    list_display = (
        "id",
        "image_display",
        "description",
    )
    search_fields = ("description",)
    list_filter = [
        ("camera__model", DropdownFilter),
    ]
    autocomplete_fields = ("camera",)

    image_display = AdminThumbnail(image_field="file")
    image_display.short_description = "Image"
    readonly_fields = ["image_display"]

    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 100})}}


class CameraFilesAdmin(CommonAdmin):
    list_display = (
        "id",
        "file",
        "description",
    )
    search_fields = ("description",)
    list_filter = [
        ("camera__model", DropdownFilter),
    ]
    autocomplete_fields = ("camera",)
    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 100})}}


class LensPicturesAdmin(CommonAdmin):
    list_display = (
        "id",
        "image_display",
        "description",
    )
    search_fields = ("description",)
    list_filter = [
        ("lens__model", DropdownFilter),
    ]
    autocomplete_fields = ("lens",)

    image_display = AdminThumbnail(image_field="file")
    image_display.short_description = "Image"
    readonly_fields = ["image_display"]

    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 100})}}


class LensFilesAdmin(CommonAdmin):
    list_display = (
        "id",
        "file",
        "description",
    )
    search_fields = ("description",)
    list_filter = [
        ("lens__model", DropdownFilter),
    ]
    autocomplete_fields = ("lens",)
    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 100})}}


admin.site.register(CameraFile, CameraFilesAdmin)
admin.site.register(CameraPicture, CameraPicturesAdmin)
admin.site.register(LensFile, LensFilesAdmin)
admin.site.register(LensPicture, LensPicturesAdmin)
