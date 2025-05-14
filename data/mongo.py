# db/mongo.py
from pymongo import MongoClient

def get_database():
    """
    Connects to local MongoDB and returns the risk_app database.
    """
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    return client["risk_app"]

def get_collection(collection_name):
    """
    Helper to get a specific collection (e.g., 'portfolios').
    """
    db = get_database()
    return db[collection_name]
