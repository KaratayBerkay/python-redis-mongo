import datetime

from bson import ObjectId
from .mongo_conn import MongoMixin
from typing import List, Dict, Union


class MongoActions(MongoMixin):
    def __init__(self):
        super().__init__()

    def insert(self, data: Union[List, Dict]):
        if isinstance(data, dict):
            return self.collection.insert_one(document=data)
        elif isinstance(data, list):
            return self.collection.insert_many(documents=data)
        return None

    def find(self, dict_filter: dict):
        find_results = []
        if "id" in dict_filter:
            dict_filter["_id"] = ObjectId(dict_filter.pop("id"))
        for find_result in list(self.collection.find(filter=dict_filter)):
            find_result["id"] = ObjectId(find_result.pop("_id")).__str__()
            find_results.append(find_result)
        return find_results

    def update(self, dict_filter: Dict, data: Union[List, Dict]):
        if "id" in dict_filter:
            dict_filter["_id"] = ObjectId(dict_filter.pop("id"))
        if isinstance(data, dict):
            return self.collection.update_one(filter=dict_filter, update={"$set": data})
        elif isinstance(data, list):
            return self.collection.update_many(
                filter=dict_filter, update={"$set": data}
            )
        return None

    def delete(self, dict_filter: Dict):
        if "id" in dict_filter:
            dict_filter["_id"] = ObjectId(dict_filter.pop("id"))
        return self.collection.delete_many(filter=dict_filter)
