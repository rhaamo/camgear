from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from .validators import validate_picture, validate_other

from controllers.gear.models import Camera, Lens


class CameraPicture(models.Model):
    camera = models.ForeignKey(
        Camera, related_name="camera_pictures", blank=False, null=False, on_delete=models.CASCADE
    )

    description = models.CharField(max_length=255, blank=True, null=True)

    file = models.ImageField(upload_to="pictures/", validators=[validate_picture], blank=False, null=False)

    file_mini = ImageSpecField(
        source="file", processors=[ResizeToFit(50, 50, upscale=False)], format="JPEG", options={"quality": 80}
    )
    file_small = ImageSpecField(
        source="file", processors=[ResizeToFit(200, 150, upscale=False)], format="JPEG", options={"quality": 80}
    )
    file_medium = ImageSpecField(
        source="file", processors=[ResizeToFit(400, 400, upscale=False)], format="JPEG", options={"quality": 80}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ("id",)
        verbose_name = "Camera Picture"
        verbose_name_plural = "Camera Pictures"

    def __str__(self):
        return self.description or "No description"


class CameraFile(models.Model):
    camera = models.ForeignKey(Camera, related_name="camera_files", blank=False, null=False, on_delete=models.CASCADE)

    description = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="files/", validators=[validate_other], blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ("id",)
        verbose_name = "Camera File"
        verbose_name_plural = "Camera Files"

    def __str__(self):
        return self.description or "No description"


class LensPicture(models.Model):
    lens = models.ForeignKey(Lens, related_name="lens_pictures", blank=False, null=False, on_delete=models.CASCADE)

    description = models.CharField(max_length=255, blank=True, null=True)

    file = models.ImageField(upload_to="pictures/", validators=[validate_picture], blank=False, null=False)

    file_mini = ImageSpecField(
        source="file", processors=[ResizeToFit(50, 50, upscale=False)], format="JPEG", options={"quality": 80}
    )
    file_small = ImageSpecField(
        source="file", processors=[ResizeToFit(200, 150, upscale=False)], format="JPEG", options={"quality": 80}
    )
    file_medium = ImageSpecField(
        source="file", processors=[ResizeToFit(400, 400, upscale=False)], format="JPEG", options={"quality": 80}
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ("id",)
        verbose_name = "Lens Picture"
        verbose_name_plural = "Lens Pictures"

    def __str__(self):
        return self.description or "No description"


class LensFile(models.Model):
    lens = models.ForeignKey(Lens, related_name="lens_files", blank=False, null=False, on_delete=models.CASCADE)

    description = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="files/", validators=[validate_other], blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ("id",)
        verbose_name = "Lens File"
        verbose_name_plural = "Lens Files"

    def __str__(self):
        return self.description or "No description"
