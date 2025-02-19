from flask import Blueprint, request, jsonify 
from app.schemas.pokemon_favorite_schema import PokemonFavoriteSchema 
from marshmallow import ValidationError
from app.models.factory import ModelFactory 
from bson import ObjectId 


bd = Blueprint("pokemon_favorite", __name__, url_prefix="/pokemon_favorite")
pokemon_favorite_schema = PokemonFavoriteSchema() 
pokemon_favorite_model = ModelFactory.get_model("pokemon_favorites") 

#Ruta para crear un pokemon favorito
@bd.route("/create", methods = ["POST"])
def create():
    try:
        data = pokemon_favorite_schema.load(request.json) 
        pokemon_favorite_id = pokemon_favorite_model.create(data)  
        return jsonify({pokemon_favorite_id:str(pokemon_favorite_id)}), 200 

#Validar los datos enviados
    except ValidationError as err:
        return jsonify("Los datos son incorrectos"), 400 
    
#Ruta para eliminar un pokemon favorito
@bd.route("/delete/<string:pokemon_favorite_id>", methods=["DELETE"])
def delete(pokemon_favorite_id):
    pokemon_favorite_model.delete(ObjectId(pokemon_favorite_id))
    return jsonify("Pokemon eliminado con éxito"), 200