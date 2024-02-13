from pymongo import MongoClient

mongo_client = MongoClient(
    username='mongo_user',
    password='mongo_password',
    host='mongo',
    port=27017,
    document_class=dict,
    connect=True
)
