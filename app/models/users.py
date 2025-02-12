from app import mongo

#creamos la clase usuario
class User:
    collection = mongo.db.users

#encaontrar todos los usuarios
    @staticmethod
    def find_all():
        users = User.collection.find()
        return list(users)

#encontrar por id
    @staticmethod
    def find_by_id(user_id):
        user = User.collection.find_one({
            "id": user_id
        })
        return user

#crear un usuario
    @staticmethod
    def create(user_data):
        user = User.collection.insert_one(user_data)
        return user.inserted_id

#actualizar un usuario
    @staticmethod
    def update(user_id, data):
        user = User.collection.update_one({
            "id": user_id
        }, {
            "$set": data
        })
        return user

#eliminar un usuario
    @staticmethod
    def delete(user_id):
        user = User.collection.delete_one({"id": user_id})