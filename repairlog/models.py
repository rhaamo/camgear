from django.db import models
from gear.models import Body, Lens, Accessory
from datetime import datetime


class BodyRepairLog(models.Model):
    title = models.CharField(max_length=255, blank=False, default="Repair log")
    note = models.TextField(blank=False)
    done_at = models.DateTimeField(blank=False, default=datetime.now)
    private = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    body = models.ForeignKey(
        Body,
        related_name="body_repairlog",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ("-done_at",)
        verbose_name_plural = "Repair Logs"

    def __str__(self):
        return f"Repair log on {self.created_at.strftime('%Y/%m/%d')}"


class LensRepairLog(models.Model):
    title = models.CharField(max_length=255, blank=False, default="Repair log")
    note = models.TextField(blank=False)
    done_at = models.DateTimeField(blank=False, default=datetime.now)
    private = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    body = models.ForeignKey(
        Lens,
        related_name="lens_repairlog",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ("-done_at",)
        verbose_name_plural = "Repair Logs"

    def __str__(self):
        return f"Repair log on {self.created_at.strftime('%Y/%m/%d')}"


class AccessoryRepairLog(models.Model):
    title = models.CharField(max_length=255, blank=False, default="Repair log")
    note = models.TextField(blank=False)
    done_at = models.DateTimeField(blank=False, default=datetime.now)
    private = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    body = models.ForeignKey(
        Accessory,
        related_name="accessory_repairlog",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ("-done_at",)
        verbose_name_plural = "Repair Logs"

    def __str__(self):
        return f"Repair log on {self.created_at.strftime('%Y/%m/%d')}"
