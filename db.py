from pymongo import MongoClient

# creating connections for communicating with Mongo DB
client = MongoClient('localhost', 27017)
db = client["banco"]
collection = db["employees"]


# Function to insert data into mongo db
def insert(document):
    try:
        return collection.insert_one(document)

    except Exception as e:
        return str(e)


# Function to update record to mongo db
def update(id, document):
    try:
        return collection.update_one(id, document)

    except Exception as e:
        return str(e)


# function to read records from mongo db
def read():
    try:
        return collection.find()

    except Exception as e:
        return str(e)


# Function to delete record from mongo db
def delete(id):
    try:
        return collection.delete_many(id)

    except Exception as e:
        print(str(e))
