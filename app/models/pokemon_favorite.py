from app import mongo 
from app.models.super_clase import SuperClase

class PokemonSaved(SuperClase):
    def __init__(self):
        super().__init__("pokemons_favorites")
    
    