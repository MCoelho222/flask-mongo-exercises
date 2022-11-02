from flasgger import Swagger
from flask import Flask

def create_swagger(app: Flask):
    app.config['SWAGGER'] = {
        "openapi": "3.0.0",
        "title": "Api de Filmes",
        "description": "Api para trazer dados dos melhores filmes da história"
    }

    Swagger(app)