from django.contrib import admin
from .models import System, Manufacturer, BodyUrl
from camgear.common import CommonAdmin


class SystemAdmin(CommonAdmin):
    list_filter = ("manufacturers",)
    search_fields = ("name",)


class ManufacturerAdmin(CommonAdmin):
    search_fields = ("name",)


class BodyUrlAdmin(CommonAdmin):
    search_fields = ("url",)


admin.site.register(System, SystemAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
# admin.site.register(BodyUrl, BodyUrlAdmin)
