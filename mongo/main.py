import random

from pymongo import MongoClient

mongo_conn_details = {"host": "localhost", "port": 27017, "db_name": "mongo"}


class MongoConnection:
    def __init__(self):
        self.client = MongoClient(
            mongo_conn_details["host"],
            mongo_conn_details["port"],
            uuidRepresentation="standard",
        )
        self.db = self.client[mongo_conn_details["db_name"]]

    def __del__(self):
        self.client.close()

    def create_collection(self, collection_name):
        existing_collections = self.db.list_collection_names()
        if collection_name not in existing_collections:
            self.db.create_collection(collection_name)

    def insert_one(self, collection_name, document):
        collection = self.db[collection_name]
        collection.insert_one(document)

    def insert_many(self, collection_name, documents):
        collection = self.db[collection_name]
        collection.insert_many([doc for doc in documents])

    def clear_table(self, collection_name):
        collection = self.db[collection_name]
        collection.drop()


mongo = MongoConnection()
mongo.create_collection("test_collection")
mongo.clear_table("test_collection")
collection = mongo.db["test_collection"]

mongo.insert_one("test_collection", {"id": 1, "data": "test"})

data_list = [{"id": id, f"data_{id}": "test"} for id in range(2, 100)]

mongo.insert_many("test_collection", data_list)

cursor = collection.find({"id": {"$gt": 97}})
print(list(cursor))

mongo.clear_table("test_collection")

data_list = [
    {"film_id": random.randint(1, 10), f"rating": random.randint(1, 100)}
    for _ in range(1, 10_001)
]
mongo.insert_many("test_collection", data_list)

for film_id in range(1, 10):
    pipeline = [
        {"$match": {"film_id": film_id}},
        {"$group": {"_id": "$film_id", "average_rating": {"$avg": "$rating"}}},
    ]
    result = collection.aggregate(pipeline)
    for row in result:
        print(row)
