import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load variables from .env
load_dotenv()

# Read values
MONGODB_URI = os.getenv("MONGODB_URI")
DATABASE_NAME = os.getenv("DATABASE_NAME")

# Connect to MongoDB Atlas
client = MongoClient(MONGODB_URI)

# Select database
db = client[DATABASE_NAME]

# Collections
employees_collection = db["employees"]
users_collection = db["users"]

print(" Connected to MongoDB Atlas")