from src.app import app, mongo_client
from src.app.routes import routes
from src.app.models.combats import create_collection_combats
from src.app.models.pokemons import create_collection_pokemons
from flask.cli import with_appcontext
import click

routes(app)

@click.command(name="create_collections")
@with_appcontext
def call_command():
    create_collection_combats(mongo_client)
    create_collection_pokemons(mongo_client)
app.cli.add_command(call_command)


if __name__ == "__main__":
    app.run()