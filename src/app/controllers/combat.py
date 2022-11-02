from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util

combats = Blueprint("combats", __name__, url_prefix="/combats")

@combats.route("/get_all_combats", methods=["GET"])
def get_all_combats():
    combats = mongo_client.combats.aggregate([{
        "$match": {
            "type": "Movie"
        }
    }])
    return Response(
        response=json_util.dumps({"records": combats}),
        status=200,
        mimetype='application/json'
    )