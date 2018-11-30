from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_babelex import gettext
from flask_security import login_required, current_user
from flask_uploads import UploadSet
import os

from forms import CameraAddForm, CameraEditForm
from models import db, Camera
from utils import IMAGES, get_hashed_filename

bp_cameras = Blueprint("bp_cameras", __name__)

pictures = UploadSet("pictures", IMAGES)


@bp_cameras.route("/gear/camera/add", methods=["GET", "POST"])
@login_required
def new():
    pcfg = {"title": gettext("Add Camera")}

    form = CameraAddForm()
    if form.validate_on_submit():
        camera = Camera()
        camera.state = form.state.data
        camera.state_notes = form.state_notes.data

        camera.manufacturer = form.manufacturer.data
        camera.model = form.model.data
        camera.model_notes = form.model_notes.data
        camera.description = form.description.data
        camera.serial = form.serial.data
        camera.mount = form.mount.data

        camera.camera_type = form.camera_type.data

        camera.film_type = form.film_type.data
        camera.auto_expo = form.auto_expo.data
        camera.auto_focus = form.auto_focus.data
        camera.batteries = form.batteries.data
        camera.hot_shoe = form.hot_shoe.data
        camera.fixed_lense = form.fixed_lense.data

        camera.iso_min = form.iso_min.data
        camera.iso_max = form.iso_max.data
        camera.focale = form.focale.data
        camera.min_aperture = form.min_aperture.data
        camera.max_aperture = form.max_aperture.data
        camera.blades = form.blades.data
        camera.filter_diameter = form.filter_diameter.data
        camera.weight = form.weight.data
        camera.length = form.length.data
        camera.focus = form.focus.data
        camera.focus_length = form.focus_length.data
        camera.macro = form.macro.data
        camera.macro_length = form.macro_length.data

        camera.private = form.private.data

        camera.url1 = form.url1.data
        camera.url2 = form.url2.data
        camera.url3 = form.url3.data

        camera.user_id = current_user.id

        if "picture" in request.files:
            camera.pic_filename = get_hashed_filename(request.files["picture"].filename)
            pictures.save(
                request.files["picture"], folder=current_app.config["UPLOADED_PICTURES_DEST"], name=camera.pic_filename
            )

        db.session.add(camera)
        db.session.commit()
        flash("Successfully added camera.", "success")
        return redirect(url_for("bp_users.cameras", name=current_user.name))
    return render_template("cameras/new.jinja2", pcfg=pcfg, form=form)


@bp_cameras.route("/gear/camera/<int:camera_id>/edit", methods=["GET", "POST"])
@login_required
def edit(camera_id):
    pcfg = {"title": gettext("Edit Camera")}

    camera = Camera.query.filter(Camera.id == camera_id, Camera.user_id == current_user.id).first()
    if not camera:
        flash("Camera not found", "error")
        return redirect(url_for("bp_users.cameras", name=current_user.name))

    form = CameraEditForm(request.form, obj=camera)

    if form.validate_on_submit():
        form.populate_obj(camera)

        if "picture" in request.files:
            camera.pic_filename = get_hashed_filename(request.files["picture"].filename)
            pictures.save(
                request.files["picture"], folder=current_app.config["UPLOADED_PICTURES_DEST"], name=camera.pic_filename
            )

        db.session.commit()
        flash("Successfully edited camera.", "success")
        return redirect(url_for("bp_users.cameras", name=current_user.name))

    # For some reasons the private.data isn't populated and stay to False even if camera.private == True
    form.private.data = camera.private
    form.auto_expo.data = camera.auto_expo
    form.auto_focus.data = camera.auto_focus
    form.hot_shoe.data = camera.hot_shoe
    form.fixed_lense.data = camera.fixed_lense
    form.blades.data = camera.blades
    form.macro.data = camera.macro

    return render_template("cameras/edit.jinja2", pcfg=pcfg, form=form, camera=camera)


@bp_cameras.route("/gear/camera/<int:camera_id>/delete", methods=["GET", "POST", "PUT"])
@login_required
def delete(camera_id):
    camera = Camera.query.filter(Camera.id == camera_id, Camera.user_id == current_user.id).first()
    if not camera:
        flash("Camera not found", "error")
        return redirect(url_for("bp_users.cameras", name=current_user.name))

    pic_filename = camera.pic_filename

    db.session.delete(camera)
    db.session.commit()

    f = os.path.join(current_app.config["UPLOADED_PICTURES_DEST"], pic_filename)
    if os.path.isfile(f):
        os.remove(f)

    flash("Successfully deleted camera", "success")
    return redirect(url_for("bp_users.cameras", name=current_user.name))
