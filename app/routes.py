from flask import Blueprint, send_from_directory
from app import oidc

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/<path:filename>")
@oidc.require_login
def static_web(filename="index.html"):
    return send_from_directory("../FHH/html", filename)

@main.route("/<folder>/<path:filename>")
def static_files(folder, filename):
    return send_from_directory("../FHH/" + folder, filename)
