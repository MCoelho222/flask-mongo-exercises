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

@pokemons.route("/more_victories_over_7", methods=['GET'])
def list_more_vitories_over_seven():
    winners = mongo_client.pokemons.aggregate([
    {
        '$lookup': {
            'from': 'combats', 
            'as': 'Winners', 
            'let': {
                'id_pokemon': '$#'
            }, 
            'pipeline': [
                {
                    '$match': {
                        '$expr': {
                            '$and': [
                                {
                                    '$eq': [
                                        '$Winner', '$$id_pokemon'
                                    ]
                                }, {
                                    '$or': [
                                        {
                                            '$eq': [
                                                '$First_pokemon', 7
                                            ]
                                        }, {
                                            '$eq': [
                                                '$Second_pokemon', 7
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                }
            ]
        }
    }, {
        '$match': {
            'Winners.0': {
                '$exists': True
            }, 
            '#': {
                '$ne': 7
            }
        }
    }, {
        '$project': {
            '_id': 0,
            '#': 1, 
            'Name': 1, 
            'Victories': {
                '$size': '$Winners'
            }
        }
    }, {
        '$sort': {
            'Victories': -1
        }
    }, {
        '$limit': 10
    }
    ])
    return Response(
        response=json_util.dumps({"records": winners}),
        status=200,
        mimetype='application/json'
    )

