from flask import Blueprint, jsonify, request
from flask_security import login_required, current_user
from models import db, Camera, Lens, Accessory

bp_autocomplete = Blueprint("bp_autocomplete", __name__)

# Currently, the search query isn't used at all for filtering since there is huge changes that any query won't return
# A shitton of results, that /will/ change, but for now, just returns anything groupped


@bp_autocomplete.route("/api/autocomplete/manufacturer", methods=["GET", "POST"])
@login_required
def manufacturer():
    # From: Camera, Lens and Accessories
    # Only current_user
    s = request.args.get("query")

    cam = db.session.query(Camera.manufacturer).filter(Camera.user_id == current_user.id).group_by(Camera.manufacturer)
    lens = db.session.query(Lens.manufacturer).filter(Camera.user_id == current_user.id).group_by(Lens.manufacturer)
    acc = (
        db.session.query(Accessory.manufacturer)
        .filter(Camera.user_id == current_user.id)
        .group_by(Accessory.manufacturer)
    )
    all = cam.union(lens).union(acc).all()
    return jsonify({"query": s, "suggestions": [i[0] for i in all]})


@bp_autocomplete.route("/api/autocomplete/mount", methods=["GET", "POST"])
@login_required
def mount():
    # From: Camera, Lens and Accessories
    # Only current_user
    s = request.args.get("query")

    cam = db.session.query(Camera.mount).filter(Camera.user_id == current_user.id).group_by(Camera.mount)
    lens = db.session.query(Lens.mount).filter(Camera.user_id == current_user.id).group_by(Lens.mount)
    acc = db.session.query(Accessory.mount).filter(Camera.user_id == current_user.id).group_by(Accessory.mount)
    all = cam.union(lens).union(acc).all()
    return jsonify({"query": s, "suggestions": [i[0] for i in all]})


@bp_autocomplete.route("/api/autocomplete/batteries", methods=["GET", "POST"])
@login_required
def batteries():
    # From: Camera and Accessories
    # Only current_user
    s = request.args.get("query")

    cam = db.session.query(Camera.batteries).filter(Camera.user_id == current_user.id).group_by(Camera.batteries)
    acc = db.session.query(Accessory.batteries).filter(Camera.user_id == current_user.id).group_by(Accessory.batteries)
    all = cam.union(acc).all()
    return jsonify({"query": s, "suggestions": [i[0] for i in all]})


@bp_autocomplete.route("/api/autocomplete/model", methods=["GET", "POST"])
@login_required
def model():
    # From: Camera, Lens and Accessories
    # Only current_user
    s = request.args.get("query")

    cam = db.session.query(Camera.model).filter(Camera.user_id == current_user.id).group_by(Camera.model)
    lens = db.session.query(Lens.model).filter(Camera.user_id == current_user.id).group_by(Lens.model)
    acc = db.session.query(Accessory.model).filter(Camera.user_id == current_user.id).group_by(Accessory.model)
    all = cam.union(lens).union(acc).all()
    return jsonify({"query": s, "suggestions": [i[0] for i in all]})
