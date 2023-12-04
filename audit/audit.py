import time
import uuid
from datetime import datetime

from flask_openapi3 import APIBlueprint

from utils import *
from app import db
from flask import jsonify
from models import *
from pydantic_models import *

bp = APIBlueprint("audit", __name__, url_prefix="/audit")


@bp.get("/get_system_components")
def system_components():
    system_components = items_to_dict(SystemComponent.query.all())
    return jsonify({"components": system_components})


@bp.get("/get_project_components")
def project_components():
    project_components = items_to_dict(ProjectComponent.query.all())
    return jsonify({"components": project_components})


@bp.get("/get_actions")
def actions():
    actions = items_to_dict(Action.query.all())
    return jsonify({"actions": actions})


@bp.get("/system_changes")
def get_system_changes():
    changes_component = items_to_dict(SystemChange.query.all())
    return jsonify({"system_changes": changes_component})


@bp.get("/project_changes")
def get_project_changes():
    changes_component = items_to_dict(ProjectChange.query.all())
    return jsonify({"project_changes": changes_component})


@bp.get("/playlist")
def get_playlists():
    playlists = items_to_dict(Playlist.query.all())
    return jsonify({"playlists": playlists})


@bp.post("/system_changes")
def system_changes(form: ChangeComponent):
    change_component = SystemChange(id=str(uuid.uuid4()),
                                    id_action=form.id_action,
                                    id_component=form.id_component,
                                    id_user=form.id_user,
                                    new_value=form.new_value,
                                    old_value=form.old_value,
                                    date=datetime.fromtimestamp(time.time()))
    db.session.add(change_component)
    db.session.flush()
    db.session.commit()
    return jsonify(200)


@bp.post("/project_changes")
def project_changes(form: ChangeComponent):
    project_component = ProjectChange(id=str(uuid.uuid4()),
                                      id_action=form.id_action,
                                      id_component=form.id_component,
                                      id_user=form.id_user,
                                      new_value=form.new_value,
                                      old_value=form.old_value,
                                      date=datetime.fromtimestamp(time.time()))
    db.session.add(project_component)
    db.session.flush()
    db.session.commit()
    return jsonify(200)

