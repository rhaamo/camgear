from django.contrib import admin
from .models import System, Manufacturer
from camgear.common import CommonAdmin
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.db import models
from django.contrib.admin.widgets import FilteredSelectMultiple

class SystemAdmin(CommonAdmin):
    list_filter = ("manufacturers",)
    search_fields = ("name",)

    formfield_overrides = {
        models.ManyToManyField: {'widget': FilteredSelectMultiple('Manufacturers', is_stacked=False)}
    }


class ManufacturerAdmin(CommonAdmin):
    search_fields = ("name",)


class BodyUrlAdmin(CommonAdmin):
    search_fields = ("url",)


admin.site.register(System, SystemAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
