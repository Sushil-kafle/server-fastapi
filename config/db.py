from pymongo import MongoClient
from decouple import config
import os


mongoURI= os.getenv("MONGO_URI")

client = os.getenv("CLIENT_URL")
# Connect to the MongoDB server
db = client["discussion"]
User = db["users"]

Course = db["courses"]
News = db['news']


