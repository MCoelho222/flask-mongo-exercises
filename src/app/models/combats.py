from src.app.utils import get_validator_json

def create_collection_combats(mongo_client):
  combats_validator = get_validator_json("validators","combat")

  try:
    mongo_client.create_collection("combats")
  except Exception as e:
    print(e)

  mongo_client.command("collMod", "combats", validator=combats_validator)
  # mongo_client.combats.insert_many(get_validator_json("db","combat"))