from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_babelex import gettext
from flask_security import login_required, current_user
from flask_uploads import UploadSet
import os

from forms import LensAddForm, LensEditForm
from models import db, Lens
from utils import IMAGES, get_hashed_filename

bp_lenses = Blueprint("bp_lenses", __name__)

pictures = UploadSet("pictures", IMAGES)


@bp_lenses.route("/gear/lens/add", methods=["GET", "POST"])
@login_required
def new():
    pcfg = {"title": gettext("Add Lens")}

    form = LensAddForm()
    if form.validate_on_submit():
        lens = Lens()
        lens.state = form.state.data
        lens.state_notes = form.state_notes.data

        lens.manufacturer = form.manufacturer.data
        lens.model = form.model.data
        lens.model_notes = form.model_notes.data
        lens.description = form.description.data
        lens.serial = form.serial.data
        lens.mount = form.mount.data

        lens.focale = form.focale.data
        lens.min_aperture = form.min_aperture.data
        lens.max_aperture = form.max_aperture.data
        lens.lens_type = form.lens_type.data
        lens.macro = form.macro.data
        lens.macro_length = form.macro_length.data
        lens.filter_diameter = form.filter_diameter.data
        lens.blades = form.blades.data
        lens.angle = form.angle.data
        lens.focus = form.focus.data
        lens.focus_length = form.focus_length.data
        lens.weight = form.weight.data
        lens.length = form.length.data

        lens.private = form.private.data

        lens.url1 = form.url1.data
        lens.url2 = form.url2.data
        lens.url3 = form.url3.data

        lens.user_id = current_user.id

        if "picture" in request.files:
            lens.pic_filename = get_hashed_filename(request.files["picture"].filename)
            pictures.save(
                request.files["picture"], folder=current_app.config["UPLOADED_PICTURES_DEST"], name=lens.pic_filename
            )

        db.session.add(lens)
        db.session.commit()
        flash("Successfully added lens.", "success")
        return redirect(url_for("bp_users.lens", name=current_user.name))
    return render_template("lenses/new.jinja2", pcfg=pcfg, form=form)


@bp_lenses.route("/gear/lens/<int:lens_id>/edit", methods=["GET", "POST"])
@login_required
def edit(lens_id):
    pcfg = {"title": gettext("Edit Lens")}

    lens = Lens.query.filter(Lens.id == lens_id, Lens.user_id == current_user.id).first()
    if not lens:
        flash("Lens not found", "error")
        return redirect(url_for("bp_users.lenses", name=current_user.name))

    form = LensEditForm(request.form, obj=lens)
    if form.validate_on_submit():
        form.populate_obj(lens)

        if "picture" in request.files:
            lens.pic_filename = get_hashed_filename(request.files["picture"].filename)
            pictures.save(
                request.files["picture"], folder=current_app.config["UPLOADED_PICTURES_DEST"], name=lens.pic_filename
            )

        db.session.commit()
        flash("Successfully edited lens.", "success")
        return redirect(url_for("bp_users.lenses", name=current_user.name))

    # For some reasons the private.data isn't populated and stay to False even if lens.private == True
    form.private.data = lens.private
    form.macro.data = lens.macro
    form.blades.data = lens.blades

    return render_template("lenses/edit.jinja2", pcfg=pcfg, form=form, lens=lens)


@bp_lenses.route("/gear/lens/<int:lens_id>/delete", methods=["GET", "POST", "PUT"])
@login_required
def delete(lens_id):
    lens = Lens.query.filter(Lens.id == lens_id, Lens.user_id == current_user.id).first()
    if not lens:
        flash("Lens not found", "error")
        return redirect(url_for("bp_users.lens", name=current_user.name))

    pic_filename = lens.pic_filename

    db.session.delete(lens)
    db.session.commit()

    if pic_filename:
        f = os.path.join(current_app.config["UPLOADED_PICTURES_DEST"], pic_filename)
        print(f"Removing: {f}")
        if os.path.isfile(f):
            os.remove(f)
        thumb_filename, thumb_ext = os.path.splitext(pic_filename)
        thumbf = os.path.join(current_app.config["UPLOADED_PICTURES_DEST"], thumb_filename + "_200x200_aaa_90.jpg")
        print(f"Removing: {thumbf}")
        if os.path.isfile(thumbf):
            os.remove(thumbf)

    flash("Successfully deleted lens", "success")
    return redirect(url_for("bp_users.lenses", name=current_user.name))
