from pymongo import MongoClient

mongo_client = MongoClient(
    "mongodb://mongo_user:mongo_password@mongo:27017/mongo_database",
    document_class=dict,
    connect=True,
)
