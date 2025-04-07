from flask import jsonify, Blueprint


bp = Blueprint("healthz", __name__)


@bp.route("/healthz", methods=["GET"])
def health_check():
    """Returns a 200 OK status for health checks."""
    return jsonify({"status": "OK"}), 200
