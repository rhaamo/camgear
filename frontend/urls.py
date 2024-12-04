from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("system/<str:name>", views.system, name="system"),
    path("manufacturer/<str:name>", views.manufacturer, name="manufacturer"),
    path("body/<uuid:uuid>", views.body, name="body"),
    path("lens/<uuid:uuid>", views.lens, name="lens"),
    path("accessory/<uuid:uuid>", views.accessory, name="accessory"),
]
