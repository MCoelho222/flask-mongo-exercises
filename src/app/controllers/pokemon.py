from flask import Blueprint
from flask.wrappers import Response
from src.app import mongo_client
from bson import json_util

pokemons = Blueprint("pokemons", __name__, url_prefix="/pokemons")

@pokemons.route("/list_all_generation_one", methods=["GET"])
def list_all_generation_one_5x_winner_least():
    pokemons = mongo_client.pokemons.aggregate([
    {
        '$match': {
            'Generation': 1
        }
    }, {
        '$lookup': {
            'from': 'combats', 
            'localField': '#', 
            'foreignField': 'Winner', 
            'as': 'Winners'
        }
    }, {
        '$match': {
            'Winners.5': {
                '$exists': True
            }
        }
    }, {
        '$project': {
            '_id': 1, 
            'Name': 1, 
            'Generation': 1
        }
    }, {
        '$limit': 10
    }
])
    return Response(
        response=json_util.dumps({"records": pokemons}),
        status=200,
        mimetype='application/json'
    )