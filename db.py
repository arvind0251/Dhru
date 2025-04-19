from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["otp_bot"]
users = db["users"]
services = db["services"]
countries = db["countries"]

def init_db():
    db.command("ping")

def get_user(chat_id):
    return users.find_one({"_id": chat_id})

def create_user(chat_id, data):
    data["_id"] = chat_id
    users.insert_one(data)

def update_user(chat_id, updates):
    users.update_one({"_id": chat_id}, {"$set": updates})

def increment_user_field(chat_id, field, value):
    users.update_one({"_id": chat_id}, {"$inc": {field: value}})

def get_all_services():
    return {s["name"]: {"id": s["id"], "price": s["price"]} for s in services.find()}

def get_all_countries():
    return {c["name"]: c["code"] for c in countries.find()}

def add_service(name, sid, price):
    services.insert_one({"name": name, "id": sid, "price": price})

def add_country(name, code):
    countries.insert_one({"name": name, "code": code})
