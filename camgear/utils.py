import re

from django.core.exceptions import ImproperlyConfigured
from django.urls import re_path
from django.views.static import serve
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.html import mark_safe
from django.utils.translation import gettext as _


# We always serve static, even in production, sorry for the best practices...
def static(prefix, view=serve, **kwargs):
    """
    Return a URL pattern for serving files in debug mode.
    from django.conf import settings
    from controllers.utils import static
    urlpatterns = [
        # ... the rest of your URLconf goes here ...
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    """
    if not prefix:
        raise ImproperlyConfigured("Empty static prefix not permitted")
    return [
        re_path(r"^%s(?P<path>.*)$" % re.escape(prefix.lstrip("/")), view, kwargs=kwargs),
    ]


class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, renderer=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(
                ' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"  style="object-fit: cover;"/></a> %s '
                % (image_url, image_url, file_name, _(""))
            )
        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe("".join(output))
