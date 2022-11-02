from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util

pokemons = Blueprint("pokemons", __name__, url_prefix="/pokemons")

@pokemons.route("/list_all_generation_one", methods=["GET"])
def list_all_generation_one():
    pokemons = mongo_client.pokemons.aggregate([{
        "$match": {
            "generation": "1"
        }
    }])
    return Response(
        response=json_util.dumps({"records": pokemons}),
        status=200,
        mimetype='application/json'
    )