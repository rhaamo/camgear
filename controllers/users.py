import pytz
from flask import Blueprint, render_template, request, redirect, url_for, flash, Response, json
from flask_babelex import gettext
from flask_security import login_required, current_user

from forms import UserProfileForm
from models import db, User, UserLogging, Accessory, Lens, Camera
from utils import add_user_log

bp_users = Blueprint("bp_users", __name__)


@bp_users.route("/account/logs", methods=["GET"])
@login_required
def logs():
    level = request.args.get("level")
    pcfg = {"title": gettext("User Logs")}
    if level:
        _logs = (
            UserLogging.query.filter(UserLogging.level == level.upper(), UserLogging.user_id == current_user.id)
            .limit(100)
            .all()
        )
    else:
        _logs = UserLogging.query.filter(UserLogging.user_id == current_user.id).limit(100).all()
    return render_template("users/user_logs.jinja2", pcfg=pcfg, logs=_logs)


@bp_users.route("/account/logs/<int:log_id>/delete", methods=["GET", "DELETE", "PUT"])
@login_required
def logs_delete(log_id):
    log = UserLogging.query.filter(UserLogging.id == log_id, UserLogging.user_id == current_user.id).first()
    if not log:
        _datas = {"status": "error", "id": log_id}
    else:
        db.session.delete(log)
        db.session.commit()
        _datas = {"status": "deleted", "id": log_id}
    return Response(json.dumps(_datas), mimetype="application/json;charset=utf-8")


@bp_users.route("/account/edit", methods=["GET", "POST"])
@login_required
def edit():
    pcfg = {"title": gettext("Edit my profile")}

    user = User.query.filter(User.id == current_user.id).first()
    if not user:
        flash(gettext("User not found"), "error")
        return redirect(url_for("bp_main.home"))

    form = UserProfileForm(request.form, obj=user)
    form.timezone.choices = [[str(i), str(i)] for i in pytz.all_timezones]

    if form.validate_on_submit():
        user.timezone = form.timezone.data
        user.locale = form.locale.data
        user.display_name = form.display_name.data

        db.session.commit()

        # log
        add_user_log(user.id, user.id, "user", "info", "Edited user profile")

        flash(gettext("Profile updated"), "success")

        return redirect(url_for("bp_users.profile", name=user.name))

    return render_template("users/edit.jinja2", pcfg=pcfg, form=form, user=user)


@bp_users.route("/user/<string:name>/accessories", methods=["GET"])
def accessories(name):
    pcfg = {"title": gettext("%(username)s' accessories", username=name)}

    user = User.query.filter(User.name == name).first()
    if not user:
        flash(gettext("User not found"), "error")
        return redirect(url_for("bp_main.home"))

    acc_count = db.session.query(Accessory.id).filter(Accessory.user_id == user.id)
    cams_count = db.session.query(Camera.id).filter(Camera.user_id == user.id)
    lens_count = db.session.query(Lens.id).filter(Lens.user_id == user.id)

    if current_user.is_authenticated and user.id == current_user.id:
        acc = user.accessories
    else:
        acc = Accessory.query.filter(Accessory.user_id == user.id, Accessory.private.is_(False)).all()
        acc_count = acc_count.filter(Accessory.private.is_(False))
        cams_count = cams_count.filter(Camera.private.is_(False))
        lens_count = lens_count.filter(Lens.private.is_(False))

    acc_count = acc_count.count()
    cams_count = cams_count.count()
    lens_count = lens_count.count()

    return render_template(
        "users/accessories.jinja2",
        pcfg=pcfg,
        user=user,
        accessories=acc,
        accessories_count=acc_count,
        cameras_count=cams_count,
        lenses_count=lens_count,
    )


@bp_users.route("/user/<string:name>/cameras", methods=["GET"])
def cameras(name):
    pcfg = {"title": gettext("%(username)s' cameras", username=name)}

    user = User.query.filter(User.name == name).first()
    if not user:
        flash(gettext("User not found"), "error")
        return redirect(url_for("bp_main.home"))

    acc_count = db.session.query(Accessory.id).filter(Accessory.user_id == user.id)
    cams_count = db.session.query(Camera.id).filter(Camera.user_id == user.id)
    lens_count = db.session.query(Lens.id).filter(Lens.user_id == user.id)

    if current_user.is_authenticated and user.id == current_user.id:
        cams = user.cameras
    else:
        cams = Camera.query.filter(Camera.user_id == user.id, Camera.private.is_(False)).all()
        acc_count = acc_count.filter(Accessory.private.is_(False))
        cams_count = cams_count.filter(Camera.private.is_(False))
        lens_count = lens_count.filter(Lens.private.is_(False))

    acc_count = acc_count.count()
    cams_count = cams_count.count()
    lens_count = lens_count.count()

    return render_template(
        "users/cameras.jinja2",
        pcfg=pcfg,
        user=user,
        cameras=cams,
        accessories_count=acc_count,
        cameras_count=cams_count,
        lenses_count=lens_count,
    )


@bp_users.route("/user/<string:name>/lenses", methods=["GET"])
def lenses(name):
    pcfg = {"title": gettext("%(username)s' lenses", username=name)}

    user = User.query.filter(User.name == name).first()
    if not user:
        flash(gettext("User not found"), "error")
        return redirect(url_for("bp_main.home"))

    acc_count = db.session.query(Accessory.id).filter(Accessory.user_id == user.id)
    cams_count = db.session.query(Camera.id).filter(Camera.user_id == user.id)
    lens_count = db.session.query(Lens.id).filter(Lens.user_id == user.id)

    if current_user.is_authenticated and user.id == current_user.id:
        lens = user.lenses
    else:
        lens = Lens.query.filter(Lens.user_id == user.id, Lens.private.is_(False)).all()
        acc_count = acc_count.filter(Accessory.private.is_(False))
        cams_count = cams_count.filter(Camera.private.is_(False))
        lens_count = lens_count.filter(Lens.private.is_(False))

    acc_count = acc_count.count()
    cams_count = cams_count.count()
    lens_count = lens_count.count()

    return render_template(
        "users/lenses.jinja2",
        pcfg=pcfg,
        user=user,
        lenses=lens,
        accessories_count=acc_count,
        cameras_count=cams_count,
        lenses_count=lens_count,
    )


@bp_users.route("/user/<string:name>", methods=["GET"])
def profile(name):
    return cameras(name)


@bp_users.route("/account/serials", methods=["GET"])
@login_required
def serials():
    pcfg = {"title": gettext("My serials")}

    user = User.query.filter(User.id == current_user.id).first()
    if not user:
        flash(gettext("User not found"), "error")
        return redirect(url_for("bp_main.home"))

    sn_cameras = db.session.query(Camera.id, Camera.manufacturer, Camera.model, Camera.serial, Camera.state).filter(
        Camera.user_id == user.id, Camera.serial.isnot(None), Camera.serial != ""
    )
    sn_lenses = db.session.query(Lens.id, Lens.manufacturer, Lens.model, Lens.serial, Lens.state).filter(
        Lens.user_id == user.id, Lens.serial.isnot(None), Lens.serial != ""
    )
    sn_accessories = db.session.query(
        Accessory.id, Accessory.manufacturer, Accessory.model, Accessory.serial, Accessory.state
    ).filter(Accessory.user_id == user.id, Accessory.serial.isnot(None), Accessory.serial != "")
    all_serials = sn_cameras.union(sn_lenses).union(sn_accessories).all()

    return render_template("users/serials.jinja2", pcfg=pcfg, serials=all_serials)
