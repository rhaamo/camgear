from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_babelex import gettext
from flask_security import login_required, current_user

from forms import LenseAddForm, LenseEditForm
from models import db, Lense

bp_lenses = Blueprint("bp_lenses", __name__)


@bp_lenses.route("/gear/lense/add", methods=["GET", "POST"])
@login_required
def new():
    pcfg = {"title": gettext("Add Lense")}

    form = LenseAddForm()
    if form.validate_on_submit():
        lense = Lense()
        lense.state = form.state.data
        lense.state_notes = form.state_notes.data

        lense.manufacturer = form.manufacturer.data
        lense.model = form.model.data
        lense.model_notes = form.model_notes.data
        lense.description = form.description.data
        lense.serial = form.serial.data
        lense.mount = form.mount.data

        lense.focale = form.focale.data
        lense.min_aperture = form.min_aperture.data
        lense.max_aperture = form.max_aperture.data
        lense.lense_type = form.lense_type.data
        lense.macro = form.macro.data
        lense.macro_length = form.macro_length.data
        lense.filter_diameter = form.filter_diameter.data
        lense.blades = form.blades.data
        lense.angle = form.angle.data
        lense.focus = form.focus.data
        lense.focus_length = form.focus_length.data
        lense.weight = form.weight.data
        lense.length = form.length.data

        lense.private = form.private.data

        lense.url1 = form.url1.data
        lense.url2 = form.url2.data
        lense.url3 = form.url3.data

        lense.user_id = current_user.id

        db.session.add(lense)
        db.session.commit()
        flash("Successfully added lense.", "success")
        return redirect(url_for("bp_users.lenses", name=current_user.name))
    return render_template("lenses/new.jinja2", pcfg=pcfg, form=form)


@bp_lenses.route("/gear/lense/<int:lense_id>/edit", methods=["GET", "POST"])
@login_required
def edit(lense_id):
    pcfg = {"title": gettext("Edit Lense")}

    lense = Lense.query.filter(Lense.id == lense_id, Lense.user_id == current_user.id).first()
    if not lense:
        flash("Lense not found", "error")
        return redirect(url_for("bp_users.lenses", name=current_user.name))

    form = LenseEditForm(request.form, obj=lense)
    if form.validate_on_submit():
        lense.state = form.state.data
        lense.state_notes = form.state_notes.data

        lense.manufacturer = form.manufacturer.data
        lense.model = form.model.data
        lense.model_notes = form.model_notes.data
        lense.description = form.description.data
        lense.serial = form.serial.data
        lense.mount = form.mount.data

        lense.focale = form.focale.data
        lense.min_aperture = form.min_aperture.data
        lense.max_aperture = form.max_aperture.data
        lense.lense_type = form.lense_type.data
        lense.macro = form.macro.data
        lense.macro_length = form.macro_length.data
        lense.filter_diameter = form.filter_diameter.data
        lense.blades = form.blades.data
        lense.angle = form.angle.data
        lense.focus = form.focus.data
        lense.focus_length = form.focus_length.data
        lense.weight = form.weight.data
        lense.length = form.length.data

        lense.private = form.private.data

        lense.url1 = form.url1.data
        lense.url2 = form.url2.data
        lense.url3 = form.url3.data

        db.session.commit()
        flash("Successfully edited lense.", "success")
        return redirect(url_for("bp_users.lenses", name=current_user.name))
    return render_template("lenses/edit.jinja2", pcfg=pcfg, form=form, lense=lense)


@bp_lenses.route("/gear/lense/<int:lense_id>/delete", methods=["GET", "POST", "PUT"])
@login_required
def delete(lense_id):
    lense = Lense.query.filter(Lense.id == lense_id, Lense.user_id == current_user.id).first()
    if not lense:
        flash("Lense not found", "error")
        return redirect(url_for("bp_users.lenses", name=current_user.name))
    db.session.delete(lense)
    db.session.commit()
    flash("Successfully deleted lense", "success")
    return redirect(url_for("bp_users.lenses", name=current_user.name))
