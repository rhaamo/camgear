from django.contrib import admin
from .models import System, Manufacturer
from camgear.common import CommonAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple

class SystemAdmin(CommonAdmin):
    search_fields = ("name",)

class ManufacturerAdmin(CommonAdmin):
    search_fields = ("name",)


class BodyUrlAdmin(CommonAdmin):
    search_fields = ("url",)


admin.site.register(System, SystemAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
