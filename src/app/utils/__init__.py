import json
from flask_pymongo import PyMongo

mongo = PyMongo()

def get_validator_json(directory, collection):
  try:
    with open(f'src/app/{directory}/{collection}.json', 'r') as openFile:
      json_object = json.load(openFile)
      return json_object

  except:
    return None