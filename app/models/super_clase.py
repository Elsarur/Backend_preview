from app import mongo

class SuperClase:
    def __init__(self, collection):
        self.collection = mongo.db[collection]
