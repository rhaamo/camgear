import magic
from django.conf import settings
from django.core.exceptions import ValidationError


def validate_picture(upload):
    # Get MIME type of file using python-magic and then delete
    file_type = magic.from_buffer(upload.file.read(1024), mime=True)

    # Raise validation error if uploaded file is not an acceptable form of media
    if file_type not in settings.ITEM_ATTACHMENT_ALLOWED_PICTURES_TYPES:
        raise ValidationError(f"File type ({file_type}) not supported.")


def validate_other(upload):
    # Get MIME type of file using python-magic and then delete
    file_type = magic.from_buffer(upload.file.read(1024), mime=True)

    # Raise validation error if uploaded file is not an acceptable form of media
    if file_type not in settings.ITEM_ATTACHMENT_ALLOWED_OTHER_TYPES:
        raise ValidationError(f"File type ({file_type}) not supported.")
