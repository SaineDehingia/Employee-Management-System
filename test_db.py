from app.database import db

print("Database Name:", db.name)
print("Collections:", db.list_collection_names())