import json
import os
import hashlib

DATABASE_FILE = "database.json"

# ---------------------- HASHING ----------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------------------- LOAD DATABASE ----------------------
def load_database():
    if not os.path.exists(DATABASE_FILE):
        db = {"users": {}}
        with open(DATABASE_FILE, "w") as f:
            json.dump(db, f, indent=4)
        return db

    with open(DATABASE_FILE, "r") as f:
        return json.load(f)

# ---------------------- SAVE DATABASE ----------------------
def save_database(db):
    with open(DATABASE_FILE, "w") as f:
        json.dump(db, f, indent=4)

# ---------------------- REGISTER USER ----------------------
def register_user(username, password):
    db = load_database()

    if username in db["users"]:
        return False

    hashed = hash_password(password)

    db["users"][username] = {
        "password": hashed,
        "history": [],
        "medications": [],
        "pathways": []
    }

    save_database(db)
    return True

# ---------------------- AUTH USER ----------------------
def authenticate_user(username, password):
    db = load_database()

    if username not in db["users"]:
        return False

    hashed = hash_password(password)
    return db["users"][username]["password"] == hashed
