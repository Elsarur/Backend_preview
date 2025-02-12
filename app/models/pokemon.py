from app import mongo

#creamos la clase pokemon
class Pokemon:
    collection = mongo.db.pokemons

#encaontrar todos los poquemones 
    @staticmethod
    def find_all():
        pokemons = Pokemon.collection.find()
        return list(pokemons)
    
#encontrar por id
@staticmethod
def find_by_id(pokemon_id):
    pokemon = Pokemon.collection.find_one({
        "id": pokemon_id
    })
    return pokemon

#crear un pokemon
@staticmethod
def create(pokemon_data):
    pokemon = Pokemon.collection.insert_one(pokemon_data)
    return pokemon.inserted_id #funcion que devuelve el id del pokemon creado

#actualizar un pokemon
@staticmethod
def update(pokemon_id, data):
    pokemon = Pokemon.collection.update_one({
        "id": pokemon_id
    }, {
        "$set": data
    })
    return pokemon

#eliminar un pokemon
@staticmethod
def delete(pokemon_id):
    pokemon = Pokemon.collection.delete_one({"id": pokemon_id})