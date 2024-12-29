from django.shortcuts import render
from gear.models import Body, Lens, Accessory, System
from datas.models import Manufacturer, BodyUrl, AccessoryUrl, LenseUrl
from django.db.models import Prefetch, Count, Q
from files.models import (
    BodyPicture,
    BodyFile,
    LensPicture,
    LensFile,
    AccessoryPicture,
    AccessoryFile,
)
from repairlog.models import BodyRepairLog, LensRepairLog, AccessoryRepairLog
from django.shortcuts import get_object_or_404


def home(request):
    bodies = (
        Body.objects.filter(private=False)
        .order_by("manufacturer", "model")
        .prefetch_related(Prefetch("body_pictures", BodyPicture.objects.filter(private=False)))
    )
    lenses = Lens.objects.filter(private=False).order_by("manufacturer", "model")
    accessories = Accessory.objects.filter(private=False).order_by("manufacturer", "model")

    # for sidebar
    systems = System.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True) + Count("accessory", distinct=True) + Count("lens", distinct=True)
    )
    manufacturers = Manufacturer.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True) + Count("accessory", distinct=True) + Count("lens", distinct=True)
    )

    ctx = {
        "bodies": bodies,
        "lenses": lenses,
        "accessories": accessories,
        "systems": systems,
        "manufacturers": manufacturers,
        "bodies_count": bodies.count,
        "lenses_count": lenses.count,
        "accessories_count": accessories.count,
    }
    return render(request, "index.html", ctx)


def sellable(request):
    bodies = (
        Body.objects.filter(private=False, can_be_sold=True)
        .order_by("manufacturer", "model")
        .prefetch_related(Prefetch("body_pictures", BodyPicture.objects.filter(private=False)))
    )
    lenses = Lens.objects.filter(private=False, can_be_sold=True).order_by("manufacturer", "model")
    accessories = Accessory.objects.filter(private=False, can_be_sold=True).order_by("manufacturer", "model")

    # for sidebar
    systems = System.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True, filter=Q(body__can_be_sold=True)) + 
                    Count("accessory", distinct=True, filter=Q(accessory__can_be_sold=True)) + 
                    Count("lens", distinct=True, filter=Q(lens__can_be_sold=True))
    )
    manufacturers = Manufacturer.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True, filter=Q(body__can_be_sold=True)) + 
                    Count("accessory", distinct=True, filter=Q(accessory__can_be_sold=True)) + 
                    Count("lens", distinct=True, filter=Q(lens__can_be_sold=True))
    )

    ctx = {
        "bodies": bodies,
        "lenses": lenses,
        "accessories": accessories,
        "systems": systems,
        "manufacturers": manufacturers,
        "bodies_count": bodies.count,
        "lenses_count": lenses.count,
        "accessories_count": accessories.count,
        "sellable": True
    }
    return render(request, "index.html", ctx)


def system(request, name):
    system = get_object_or_404(System, name=name)

    bodies = (
        Body.objects.filter(private=False, system=system)
        .order_by("manufacturer", "model")
        .prefetch_related(Prefetch("body_pictures", BodyPicture.objects.filter(private=False)))
    )
    lenses = Lens.objects.filter(private=False, system=system).order_by("manufacturer", "model")
    accessories = Accessory.objects.filter(private=False, system=system).order_by("manufacturer", "model")

    # for sidebar
    systems = System.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True) + Count("accessory", distinct=True) + Count("lens", distinct=True)
    )
    manufacturers = Manufacturer.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True) + Count("accessory", distinct=True) + Count("lens", distinct=True)
    )

    ctx = {
        "bodies": bodies,
        "lenses": lenses,
        "accessories": accessories,
        "systems": systems,
        "manufacturers": manufacturers,
        "bodies_count": bodies.count,
        "lenses_count": lenses.count,
        "accessories_count": accessories.count,
    }
    return render(request, "index.html", ctx)


def manufacturer(request, name):
    manufacturer = get_object_or_404(Manufacturer, name=name)

    bodies = (
        Body.objects.filter(private=False, manufacturer=manufacturer)
        .order_by("manufacturer", "model")
        .prefetch_related(Prefetch("body_pictures", BodyPicture.objects.filter(private=False)))
    )
    lenses = Lens.objects.filter(private=False, manufacturer=manufacturer).order_by("manufacturer", "model")
    accessories = Accessory.objects.filter(private=False, manufacturer=manufacturer).order_by("manufacturer", "model")

    # for sidebar
    systems = System.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True) + Count("accessory", distinct=True) + Count("lens", distinct=True)
    )
    manufacturers = Manufacturer.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True) + Count("accessory", distinct=True) + Count("lens", distinct=True)
    )

    ctx = {
        "bodies": bodies,
        "lenses": lenses,
        "accessories": accessories,
        "systems": systems,
        "manufacturers": manufacturers,
        "bodies_count": bodies.count,
        "lenses_count": lenses.count,
        "accessories_count": accessories.count,
    }
    return render(request, "index.html", ctx)


def body(request, uuid):
    body = get_object_or_404(
        Body.objects.prefetch_related(
            Prefetch("body_pictures", BodyPicture.objects.filter(private=False)),
            Prefetch("body_files", BodyFile.objects.filter(private=False)),
            Prefetch("body_repairlog", BodyRepairLog.objects.filter(private=False)),
            Prefetch("body_urls", BodyUrl.objects.filter(private=False)),
        ),
        uuid=uuid,
    )

    # counts
    bodies = (
        Body.objects.filter(private=False)
        .order_by("manufacturer", "model")
        .prefetch_related(Prefetch("body_pictures", BodyPicture.objects.filter(private=False)))
    )
    lenses = Lens.objects.filter(private=False).order_by("manufacturer", "model")
    accessories = Accessory.objects.filter(private=False).order_by("manufacturer", "model")

    # for sidebar
    systems = System.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True) + Count("accessory", distinct=True) + Count("lens", distinct=True)
    )
    manufacturers = Manufacturer.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True) + Count("accessory", distinct=True) + Count("lens", distinct=True)
    )

    ctx = {
        "body": body,
        "bodies_count": bodies.count,
        "lenses_count": lenses.count,
        "accessories_count": accessories.count,
        "systems": systems,
        "manufacturers": manufacturers,
    }

    return render(request, "body.html", ctx)


def lens(request, uuid):
    lens = get_object_or_404(
        Lens.objects.prefetch_related(
            Prefetch("lens_pictures", LensPicture.objects.filter(private=False)),
            Prefetch("lens_files", LensFile.objects.filter(private=False)),
            Prefetch("lens_repairlog", LensRepairLog.objects.filter(private=False)),
            Prefetch("lens_urls", LenseUrl.objects.filter(private=False)),
        ),
        uuid=uuid,
    )

    # counts
    bodies = (
        Body.objects.filter(private=False)
        .order_by("manufacturer", "model")
        .prefetch_related(Prefetch("body_pictures", BodyPicture.objects.filter(private=False)))
    )
    lenses = Lens.objects.filter(private=False).order_by("manufacturer", "model")
    accessories = Accessory.objects.filter(private=False).order_by("manufacturer", "model")

    # for sidebar
    systems = System.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True) + Count("accessory", distinct=True) + Count("lens", distinct=True)
    )
    manufacturers = Manufacturer.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True) + Count("accessory", distinct=True) + Count("lens", distinct=True)
    )

    ctx = {
        "lens": lens,
        "bodies_count": bodies.count,
        "lenses_count": lenses.count,
        "accessories_count": accessories.count,
        "systems": systems,
        "manufacturers": manufacturers,
    }

    return render(request, "lens.html", ctx)


def accessory(request, uuid):
    accessory = get_object_or_404(
        Accessory.objects.prefetch_related(
            Prefetch("accessory_pictures", AccessoryPicture.objects.filter(private=False)),
            Prefetch("accessory_files", AccessoryFile.objects.filter(private=False)),
            Prefetch("accessory_repairlog", AccessoryRepairLog.objects.filter(private=False)),
            Prefetch("accessory_urls", AccessoryUrl.objects.filter(private=False)),
        ),
        uuid=uuid,
    )

    # counts
    bodies = (
        Body.objects.filter(private=False)
        .order_by("manufacturer", "model")
        .prefetch_related(Prefetch("body_pictures", BodyPicture.objects.filter(private=False)))
    )
    lenses = Lens.objects.filter(private=False).order_by("manufacturer", "model")
    accessories = Accessory.objects.filter(private=False).order_by("manufacturer", "model")

    # for sidebar
    systems = System.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True) + Count("accessory", distinct=True) + Count("lens", distinct=True)
    )
    manufacturers = Manufacturer.objects.order_by("name").annotate(
        total_count=Count("body", distinct=True) + Count("accessory", distinct=True) + Count("lens", distinct=True)
    )

    ctx = {
        "accessory": accessory,
        "bodies_count": bodies.count,
        "lenses_count": lenses.count,
        "accessories_count": accessories.count,
        "systems": systems,
        "manufacturers": manufacturers,
    }

    return render(request, "accessory.html", ctx)
