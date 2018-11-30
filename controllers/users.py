import pytz
from flask import Blueprint, render_template, request, redirect, url_for, flash, Response, json
from flask_babelex import gettext
from flask_security import login_required, current_user

from forms import UserProfileForm
from models import db, User, UserLogging
from utils import add_user_log
from flask_accept import accept_fallback

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


@bp_users.route("/user/<string:name>", methods=["GET"])
@accept_fallback
def profile(name):
    pcfg = {"title": gettext("%(username)s' profile", username=name)}

    user = User.query.filter(User.name == name).first()
    if not user:
        flash(gettext("User not found"), "error")
        return redirect(url_for("bp_main.home"))

    return render_template("users/profile.jinja2", pcfg=pcfg, user=user)


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
    acc = user.accessories

    return render_template("users/accessories.jinja2", pcfg=pcfg, user=user, accessories=acc)
