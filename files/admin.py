from django.contrib import admin
from django.db import models
from imagekit.admin import AdminThumbnail
from django.forms import TextInput
from camgear.common import CommonAdmin

from .models import (
    BodyFile,
    BodyPicture,
    LensFile,
    LensPicture,
    AccessoryFile,
    AccessoryPicture,
)


class BodyPicturesAdmin(CommonAdmin):
    list_display = (
        "id",
        "image_display",
        "description",
    )
    search_fields = ("description",)
    # list_filter = [
    #     ("body__model",),
    # ]
    autocomplete_fields = ("body",)

    image_display = AdminThumbnail(image_field="file")
    image_display.short_description = "Image"
    readonly_fields = ["image_display"]

    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 100})}}


class BodyFilesAdmin(CommonAdmin):
    list_display = (
        "id",
        "file",
        "description",
    )
    search_fields = ("description",)
    # list_filter = [
    #     ("body__model",),
    # ]
    autocomplete_fields = ("body",)
    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 100})}}


class LensPicturesAdmin(CommonAdmin):
    list_display = (
        "id",
        "image_display",
        "description",
    )
    search_fields = ("description",)
    # list_filter = [
    #     ("lens__model",),
    # ]
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
    # list_filter = [
    #     ("lens__model",),
    # ]
    autocomplete_fields = ("lens",)
    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 100})}}


class AccessoryPicturesAdmin(CommonAdmin):
    list_display = (
        "id",
        "image_display",
        "description",
    )
    search_fields = ("description",)
    # list_filter = [
    #     ("accessory__model",),
    # ]
    autocomplete_fields = ("lens",)

    image_display = AdminThumbnail(image_field="file")
    image_display.short_description = "Image"
    readonly_fields = ["image_display"]

    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 100})}}


class AccessoryFilesAdmin(CommonAdmin):
    list_display = (
        "id",
        "file",
        "description",
    )
    search_fields = ("description",)
    # list_filter = [
    #     ("accessory__model",),
    # ]
    autocomplete_fields = ("lens",)
    formfield_overrides = {models.CharField: {"widget": TextInput(attrs={"size": 100})}}


# admin.site.register(BodyFile, BodyFilesAdmin)
# admin.site.register(BodyPicture, BodyPicturesAdmin)
# admin.site.register(LensFile, LensFilesAdmin)
# admin.site.register(LensPicture, LensPicturesAdmin)
# admin.site.register(AccessoryFile, AccessoryFilesAdmin)
# admin.site.register(AccessoryPicture, AccessoryPicturesAdmin)
