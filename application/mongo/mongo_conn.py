import os

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database

m_user = os.getenv("MONGODB_USERNAME")
m_pass = os.getenv("MONGODB_PASSWORD")
mdata = os.getenv("MONGODB_DATABASE")
DATABASE_URL = f"mongodb://{m_user}:{m_pass}@localhost:27017/{mdata}"


class MongoMixin:
    def __init__(self):
        self.client = MongoClient(
            host=DATABASE_URL,
            document_class=dict,
            connect=True,
        )
        self.database_name = os.getenv("MONGODB_DATABASE", "mongo_database")
        self.collection_name = "mongo_collection"

        self.database: Database = self.client.get_database(self.database_name)
        self.collection: Collection = self.database[self.collection_name]
        if self.database is None:
            raise Exception("Connection error")

    @property
    def collection_lists(self):
        return self.database.list_collection_names()

    def set_collection(self, collection):
        self.collection_name = collection
        self.collection = self.database.get_collection(name=self.collection_name)

    def set_database(self, database):
        self.database_name = database
        self.database = self.client.get_database(name=self.database_name)
        self.collection = self.database.get_collection(name=self.collection_name)
