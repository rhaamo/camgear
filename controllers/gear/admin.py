from django.contrib import admin
from config.admin import CommonAdmin

from .models import Camera, Manufacturer, Mount, Lens


class CameraAdmin(CommonAdmin):
    list_display = (
        'id',
        'camera_model',
        'state',
        'mount',
        'camera_focale',
        'camera_aperture',
        'focus',
    )

    search_fields = ('name', 'state_notes', 'model_notes', 'description')

    def camera_model(self, obj):
        return obj.__str__()
    
    def camera_focale(self, obj):
        return f"{obj.focale_min or 'x'} - {obj.focale_max or 'x'}"
    
    def camera_aperture(self, obj):
        return f"{obj.min_aperture or 'x'} - {obj.max_aperture or 'x'}"

    list_filter = ('manufacturer', 'mount', 'film_type')

    fields = (
        ( 'manufacturer', 'model', 'serial', ),
        ('state', 'state_notes', 'model_notes'),
        ('description'),
        ('camera_type', 'film_type', 'mount'),
        ('batteries', 'hot_shoe', 'fixed_lens'),
        ('iso_min', 'iso_max'),
        ('focale_min', 'focale_max'),
        ('min_aperture', 'max_aperture'),
        ('blades'),
        ('filter_diameter', 'weight', 'length'),
        ('focus', 'macro', 'macro_length'),
        ('private', 'can_be_sold'),
        'url1', 'url2', 'url3'
    )

class ManufacturerAdmin(CommonAdmin):
    pass

class MountAdmin(CommonAdmin):
    pass

class LensAdmin(CommonAdmin):
    list_display = (
        'id',
        'lens_model',
        'state',
        'mount',
        'lens_focale',
        'lens_aperture',
        'focus',
    )

    search_fields = ('name', 'state_notes', 'model_notes', 'description')

    def lens_model(self, obj):
        return obj.__str__()
    
    def lens_focale(self, obj):
        return f"{obj.focale_min or 'x'} - {obj.focale_max or 'x'}"
    
    def lens_aperture(self, obj):
        return f"{obj.min_aperture or 'x'} - {obj.max_aperture or 'x'}"

    list_filter = ('manufacturer', 'mount', 'lens_type')


admin.site.register(Camera, CameraAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Mount, MountAdmin)
admin.site.register(Lens, LensAdmin)