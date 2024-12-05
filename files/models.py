from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit
from .validators import validate_picture, validate_other

from gear.models import Body, Lens, Accessory
import os
import piexif


class BodyPicture(models.Model):
    body = models.ForeignKey(
        Body,
        related_name="body_pictures",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    description = models.CharField(max_length=255, blank=True, null=True)

    file = models.ImageField(upload_to="pictures/", validators=[validate_picture], blank=False, null=False)

    file_mini = ImageSpecField(
        source="file",
        processors=[ResizeToFit(50, 50, upscale=False)],
        format="JPEG",
        options={"quality": 80},
    )
    file_small = ImageSpecField(
        source="file",
        processors=[ResizeToFit(200, 150, upscale=False)],
        format="JPEG",
        options={"quality": 80},
    )
    file_medium = ImageSpecField(
        source="file",
        processors=[ResizeToFit(400, 400, upscale=False)],
        format="JPEG",
        options={"quality": 80},
    )
    private = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ("id",)
        verbose_name = "Body Picture"
        verbose_name_plural = "Body Pictures"

    def __str__(self):
        return self.description or "No description"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Store this so we can tell if it changes in save():
        self.__original_file_name = self.file.name

    def save(self, *args, **kwargs):
        # At this point the image file has already been saved to disk.
        # Call the parent's save() method first:
        super().save(*args, **kwargs)

        if self.file and self.__original_file_name != self.file.name:
            # The file is new or changed, so edit the Exif data.
            self.sanitize_file_exif_data()

        # Re-set this in case the image has now changed:
        self.__original_file_name = self.file.name

    def sanitize_file_exif_data(self):
        "If the file image has any GPS info in its Exif data, remove it."
        if self.file:
            # Get Exif data from the file as a dict:
            exif_dict = piexif.load(self.file.path)

            if "GPS" in exif_dict and len(exif_dict["GPS"]) > 0:
                # Clear existing GPS data and put it all back to bytes:
                exif_dict["GPS"] = {}
                exif_bytes = piexif.dump(exif_dict)

                # Replace the file's existing Exif data with our modified version:
                piexif.insert(exif_bytes, self.file.path)


class BodyFile(models.Model):
    body = models.ForeignKey(
        Body,
        related_name="body_files",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    description = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="files/", validators=[validate_other], blank=False, null=False)
    private = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def filename_str(self):
        return os.path.basename(self.file.name)

    class Meta(object):
        ordering = ("id",)
        verbose_name = "Body File"
        verbose_name_plural = "Body Files"

    def __str__(self):
        return self.description or "No description"


class LensPicture(models.Model):
    lens = models.ForeignKey(
        Lens,
        related_name="lens_pictures",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    description = models.CharField(max_length=255, blank=True, null=True)

    file = models.ImageField(upload_to="pictures/", validators=[validate_picture], blank=False, null=False)

    file_mini = ImageSpecField(
        source="file",
        processors=[ResizeToFit(50, 50, upscale=False)],
        format="JPEG",
        options={"quality": 80},
    )
    file_small = ImageSpecField(
        source="file",
        processors=[ResizeToFit(200, 150, upscale=False)],
        format="JPEG",
        options={"quality": 80},
    )
    file_medium = ImageSpecField(
        source="file",
        processors=[ResizeToFit(400, 400, upscale=False)],
        format="JPEG",
        options={"quality": 80},
    )
    private = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ("id",)
        verbose_name = "Lens Picture"
        verbose_name_plural = "Lens Pictures"

    def __str__(self):
        return self.description or "No description"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Store this so we can tell if it changes in save():
        self.__original_file_name = self.file.name

    def save(self, *args, **kwargs):
        # At this point the image file has already been saved to disk.
        # Call the parent's save() method first:
        super().save(*args, **kwargs)

        if self.file and self.__original_file_name != self.file.name:
            # The file is new or changed, so edit the Exif data.
            self.sanitize_file_exif_data()

        # Re-set this in case the image has now changed:
        self.__original_file_name = self.file.name

    def sanitize_file_exif_data(self):
        "If the file image has any GPS info in its Exif data, remove it."
        if self.file:
            # Get Exif data from the file as a dict:
            exif_dict = piexif.load(self.file.path)

            if "GPS" in exif_dict and len(exif_dict["GPS"]) > 0:
                # Clear existing GPS data and put it all back to bytes:
                exif_dict["GPS"] = {}
                exif_bytes = piexif.dump(exif_dict)

                # Replace the file's existing Exif data with our modified version:
                piexif.insert(exif_bytes, self.file.path)


class LensFile(models.Model):
    lens = models.ForeignKey(
        Lens,
        related_name="lens_files",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    description = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="files/", validators=[validate_other], blank=False, null=False)
    private = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def filename_str(self):
        return os.path.basename(self.file.name)

    class Meta(object):
        ordering = ("id",)
        verbose_name = "Lens File"
        verbose_name_plural = "Lens Files"

    def __str__(self):
        return self.description or "No description"


class AccessoryPicture(models.Model):
    lens = models.ForeignKey(
        Accessory,
        related_name="accessory_pictures",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    description = models.CharField(max_length=255, blank=True, null=True)

    file = models.ImageField(upload_to="pictures/", validators=[validate_picture], blank=False, null=False)

    file_mini = ImageSpecField(
        source="file",
        processors=[ResizeToFit(50, 50, upscale=False)],
        format="JPEG",
        options={"quality": 80},
    )
    file_small = ImageSpecField(
        source="file",
        processors=[ResizeToFit(200, 150, upscale=False)],
        format="JPEG",
        options={"quality": 80},
    )
    file_medium = ImageSpecField(
        source="file",
        processors=[ResizeToFit(400, 400, upscale=False)],
        format="JPEG",
        options={"quality": 80},
    )
    private = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ("id",)
        verbose_name = "Accessory Picture"
        verbose_name_plural = "Accessory Pictures"

    def __str__(self):
        return self.description or "No description"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Store this so we can tell if it changes in save():
        self.__original_file_name = self.file.name

    def save(self, *args, **kwargs):
        # At this point the image file has already been saved to disk.
        # Call the parent's save() method first:
        super().save(*args, **kwargs)

        if self.file and self.__original_file_name != self.file.name:
            # The file is new or changed, so edit the Exif data.
            self.sanitize_file_exif_data()

        # Re-set this in case the image has now changed:
        self.__original_file_name = self.file.name

    def sanitize_file_exif_data(self):
        "If the file image has any GPS info in its Exif data, remove it."
        if self.file:
            # Get Exif data from the file as a dict:
            exif_dict = piexif.load(self.file.path)

            if "GPS" in exif_dict and len(exif_dict["GPS"]) > 0:
                # Clear existing GPS data and put it all back to bytes:
                exif_dict["GPS"] = {}
                exif_bytes = piexif.dump(exif_dict)

                # Replace the file's existing Exif data with our modified version:
                piexif.insert(exif_bytes, self.file.path)


class AccessoryFile(models.Model):
    lens = models.ForeignKey(
        Accessory,
        related_name="accessory_files",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    description = models.CharField(max_length=255, blank=True, null=True)
    file = models.FileField(upload_to="files/", validators=[validate_other], blank=False, null=False)
    private = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def filename_str(self):
        return os.path.basename(self.file.name)

    class Meta(object):
        ordering = ("id",)
        verbose_name = "Accessory File"
        verbose_name_plural = "Accessory Files"

    def __str__(self):
        return self.description or "No description"
