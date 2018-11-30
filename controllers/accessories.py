from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_babelex import gettext
from flask_security import login_required, current_user
from flask_uploads import UploadSet, IMAGES
import os

from forms import AccessoryAddForm, AccessoryEditForm
from models import db, Accessory

bp_accessories = Blueprint("bp_accessories", __name__)

pictures = UploadSet("pictures", IMAGES)


@bp_accessories.route("/gear/accessory/add", methods=["GET", "POST"])
@login_required
def new():
    pcfg = {"title": gettext("Add Accessory")}

    form = AccessoryAddForm()
    if form.validate_on_submit():
        accessory = Accessory()
        accessory.state = form.state.data
        accessory.state_notes = form.state_notes.data
        accessory.manufacturer = form.manufacturer.data
        accessory.model = form.model.data
        accessory.model_notes = form.model_notes.data
        accessory.description = form.description.data
        accessory.serial = form.serial.data
        accessory.mount = form.mount.data
        accessory.private = form.private.data
        accessory.url1 = form.url1.data
        accessory.url2 = form.url2.data
        accessory.url3 = form.url3.data
        accessory.batteries = form.batteries.data
        accessory.user_id = current_user.id

        if form.picture.data:
            accessory.pic_filename = pictures.save(form.picture.data)

        db.session.add(accessory)
        db.session.commit()
        flash("Successfully added accessory.", "success")
        return redirect(url_for("bp_users.accessories", name=current_user.name))
    return render_template("accessories/new.jinja2", pcfg=pcfg, form=form)


@bp_accessories.route("/gear/accessory/<int:accessory_id>/edit", methods=["GET", "POST"])
@login_required
def edit(accessory_id):
    pcfg = {"title": gettext("Edit Accessory")}

    accessory = Accessory.query.filter(Accessory.id == accessory_id, Accessory.user_id == current_user.id).first()
    if not accessory:
        flash("Accessory not found", "error")
        return redirect(url_for("bp_users.accessories", name=current_user.name))

    form = AccessoryEditForm(request.form, obj=accessory)

    if form.validate_on_submit():
        form.populate_obj(accessory)

        if form.picture.data:
            accessory.pic_filename = pictures.save(form.picture.data)

        db.session.commit()
        flash("Successfully edited accessory.", "success")
        return redirect(url_for("bp_users.accessories", name=current_user.name))

    # For some reasons the private.data isn't populated and stay to False even if accessory.private == True
    form.private.data = accessory.private

    return render_template("accessories/edit.jinja2", pcfg=pcfg, form=form, accessory=accessory)


@bp_accessories.route("/gear/accessory/<int:accessory_id>/delete", methods=["GET", "POST", "PUT"])
@login_required
def delete(accessory_id):
    accessory = Accessory.query.filter(Accessory.id == accessory_id, Accessory.user_id == current_user.id).first()
    if not accessory:
        flash("Accessory not found", "error")
        return redirect(url_for("bp_users.accessories", name=current_user.name))

    pic_filename = accessory.pic_filename

    db.session.delete(accessory)
    db.session.commit()

    f = os.path.join(current_app.config["UPLOADED_PICTURES_DEST"], pic_filename)
    if os.path.isfile(f):
        os.remove(f)

    flash("Successfully deleted accessory", "success")
    return redirect(url_for("bp_users.accessories", name=current_user.name))
