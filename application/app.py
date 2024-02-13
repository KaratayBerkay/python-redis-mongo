import datetime
import json
import os
import time

import pymongo.collection

from mongo_mixin import mongo_client


class App:
    def __init__(self):
        self.routes = os.getenv("ROUTES", {})

    def boot_application(self):
        path = os.getenv("PATH_INFO")
        method = os.getenv("REQUEST_METHOD")
        print("path", path)
        print("method", method)
        print("routes", self.routes)
        return {"routes": self.routes}


if __name__ == "__main__":
    app = App()
    from pymongo.collection import Collection
    while True:
        print("Mongo client initiated", mongo_client, type(mongo_client))
        try:
            database = mongo_client.mongo_database
            collection: Collection = database['new_collection']
            print("Database", database, type(database))
            print(database.list_collection_names())
            collection.insert_one({
                "name": "new_entry",
                "new_list": ["new", "list", "of", "values"],
                "new_float": 3.14,
                "new_int": 42,
                "new_bool": True,
                "new_dict": {"new_key": "new_value"},
                "new_datetime": datetime.datetime.now(tz=datetime.timezone.utc).__str__()
            })
            result = collection.find({})
            print("Result", list(result), ' | count : ', len(list(result)))
        except Exception as e:
            print("Error", e)
        app.boot_application()
        time.sleep(10)
