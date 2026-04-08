import motor.motor_asyncio
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://mongodb:27017")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URL)
database = client.library_db
collection = database.get_collection("books_collection")