from django.db import models


class States(models.IntegerChoices):
    UNKNOWN = 0, "Unknown"
    VERY_GOOD = 5, "Very Good"
    GOOD = 10, "Good"
    OK_SCRATCHES = 15, "Ok, scratches"
    NOT_SO_OK = 20, "Not so ok"
    CRACKS = 25, "Cracks"
    PARTLY_WORKING = 30, "Partly working"
    NOT_WORKING = 35, "Not working"
    LOST = 40, "Lost"
    STOLEN = 45, "Stolen"


class LensesTypes(models.IntegerChoices):
    UNKNOWN = 0, "Unknown"
    WIDE_ANGLE = 5, "Wide Angle"
    STANDARD = 10, "Standard"
    ZOOM = 15, "Zoom"
    TELEPHOTO = 20, "Telephoto"


class CamerasTypes(models.IntegerChoices):
    UNKNOWN = 0, "Unknown"
    CHAMBER = 5, "Chamber"
    CHAMBER_ST = 10, "Chamber Stereo"
    FOLDING = 15, "Folding"
    BOX = 20, "Box"
    BOX_ST = 25, "Box Stereo"
    INSTANT = 30, "Instant"
    DISPOSABLE = 35, "Disposable"
    TOY = 40, "Toy"
    PANORAMIC = 45, "Panoramic"
    POINT_AND_SHOOT = 47, "Point & Shoot"
    SLR = 48, "SLR"
    TLS = 49, "TLR"
    REFLEX_SLR = 50, "Reflex SLR"
    REFLEX_TLR = 55, "Reflex TLR"
    REFLEX_DSLR = 60, "Reflex DSLR"
    DIGITAL = 65, "Digital"
    DIGITAL = 70, "Motion picture"


class FilmTypes(models.IntegerChoices):
    UNKNOWN = 0, "Unknown"
    MM8 = 5, "8mm"
    MM9_5 = 10, "9.5mm"
    MM16 = 15, "16mm"
    MM17_5 = 20, "17.5mm"
    MM28 = 25, "28mm"
    MM30 = 30, "35mm"
    MM70 = 35, "70mm"
    MM110 = 40, "110"
    MM120 = 45, "120"
    MM126 = 50, "126"
    MM127 = 55, "127"
    MM135 = 60, "135"
    MM616 = 65, "616"
    MM628 = 70, "628"
    DISC = 75, "Disc"
    EKTACHROME = 80, "Ektachrome"
    EKTAR = 85, "Ektar"
    KODACHROME = 90, "Kodachrome"
    EASTMANCOLOR = 95, "Eastmancolor"
    PLATE = 100, "Plate"
    PACK_FILM = 105, "Pack-Film"
    PACK_FILM_100 = 110, "Pack-Film 100"
    PACK_FILM_100_80 = 115, "Pack-Film 100 or 80"
    PACK_FILM_80 = 120, "Pack-Film 80"
    SUPER_8 = 125, "Super 8"
    SINGLE_8 = 130, "Single 8"
    DOUBLE_8 = 135, "Double 8"


class FocusesTypes(models.IntegerChoices):
    UNKNOWN = 0, "Unknown"
    MANUAL = 5, "Manual"
    AUTOMATIC = 10, "Automatic"
    FIXED = 15, "Fixed"
    AUTO_MAN = 20, "Auto/Man"


class ShutterTypes(models.IntegerChoices):
    UNKNOWN = 0, "Unknown"
    CURTAINS = 5, "Curtains"
    BLADES = 10, "Blades (body)"
    BLADES_LENS = 15, "Blades (lens)"
