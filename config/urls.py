"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from controllers.utils import static

urlpatterns = [
    url(settings.ADMIN_URL, admin.site.urls),
]


admin.site.site_header = "CamGear Inventory"
admin.site.site_title = "CamGear Admin Portal"
admin.site.index_title = "Welcome to CamGear"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    print("Debug URLs enabled")
    import debug_toolbar

    urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))] + urlpatterns
    urlpatterns += staticfiles_urlpatterns()
