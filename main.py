import pymongo as pymongo
from flask import Flask, request, jsonify
from flask_objectid_converter import ObjectIDConverter
from pymongo import ReturnDocument
from pymongo.server_api import ServerApi
from bson import json_util, ObjectId
from flask_cors import CORS

#loading private connection information from environment variables
from dotenv import load_dotenv
load_dotenv()
import os
MONGODB_LINK = os.environ.get("MONGODB_LINK")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")

#connecting to mongodb
client = pymongo.MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}/?retryWrites=true&w=majority", server_api=ServerApi('1'))
#name of database
db = client.todoitem_sec1

app = Flask(__name__)
#adding an objectid type for the URL fields instead of treating it as string
#this is coming from a library we are using instead of building our own custom type
app.url_map.converters['objectid'] = ObjectIDConverter

app.config['DEBUG'] = True
#making our API accessible by any IP
CORS(app)


if __name__ == "__main__":
    app.run(port=5002)
