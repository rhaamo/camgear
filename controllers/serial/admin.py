from django.contrib import admin
from config.admin import CommonAdmin
from controllers.gear.models import Camera, Lens, Accessory


class CameraSerialsAdmin(CommonAdmin):
    """
    Create a pseudo-readonly view for Camera Serials
    """

    list_display = ("camera_model", "state", "serial")
    search_fields = ("name", "state_notes", "model_notes", "description", "serial")

    def camera_model(self, obj):
        return obj.__str__()

    list_filter = ("manufacturer", "can_be_sold")

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class LensSerialsAdmin(CommonAdmin):
    """
    Create a pseudo-readonly view for Lens Serials
    """

    list_display = ("camera_model", "state", "serial")
    search_fields = ("name", "state_notes", "model_notes", "description", "serial")

    def camera_model(self, obj):
        return obj.__str__()

    list_filter = ("manufacturer", "can_be_sold")

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class AccessorySerialsAdmin(CommonAdmin):
    """
    Create a pseudo-readonly view for Accessory Serials
    """

    list_display = ("camera_model", "state", "serial")
    search_fields = ("name", "state_notes", "model_notes", "description", "serial")

    def camera_model(self, obj):
        return obj.__str__()

    list_filter = ("manufacturer", "can_be_sold")

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class CameraSerial(Camera):
    class Meta:
        proxy = True


class LensSerial(Lens):
    class Meta:
        proxy = True


class AccessorySerial(Accessory):
    class Meta:
        proxy = True


admin.site.register(CameraSerial, CameraSerialsAdmin)
admin.site.register(LensSerial, LensSerialsAdmin)
admin.site.register(AccessorySerial, AccessorySerialsAdmin)
