from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class System(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, unique=True)
    manufacturers = models.ManyToManyField(Manufacturer, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class BodyUrl(models.Model):
    body = models.ForeignKey(
        "gear.body",
        related_name="body_urls",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    url = models.URLField(blank=False)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.url


class AccessoryUrl(models.Model):
    body = models.ForeignKey(
        "gear.accessory",
        related_name="accessory_urls",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    url = models.URLField(blank=False)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.url


class LenseUrl(models.Model):
    body = models.ForeignKey(
        "gear.lens",
        related_name="lens_urls",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    url = models.URLField(blank=False)
    private = models.BooleanField(default=False)

    def __str__(self):
        return self.url
