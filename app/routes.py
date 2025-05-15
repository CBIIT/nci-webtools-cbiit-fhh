from flask import Blueprint, send_from_directory

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/<path:filename>")
def serve_html(filename="index.html"):
    return send_from_directory("../FHH/html", filename)

@main.route("/<folder>/<path:filename>")
def serve_files(folder, filename):
    return send_from_directory("../FHH/" + folder, filename)