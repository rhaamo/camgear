from django.contrib import admin
from .models import System, Manufacturer
from camgear.common import CommonAdmin


class SystemAdmin(CommonAdmin):
    search_fields = ("name",)


class ManufacturerAdmin(CommonAdmin):
    search_fields = ("name",)


class BodyUrlAdmin(CommonAdmin):
    search_fields = ("url",)


admin.site.register(System, SystemAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
