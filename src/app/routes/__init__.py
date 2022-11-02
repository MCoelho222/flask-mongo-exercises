from flask import Flask
from src.app.controllers.combat import combats
from src.app.controllers.pokemon import pokemons


def routes(app: Flask):
  app.register_blueprint(combats)
  app.register_blueprint(pokemons)