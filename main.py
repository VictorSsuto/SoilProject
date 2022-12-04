import pymongo as pymongo
from flask import Flask, request, jsonify
from flask_objectid_converter import ObjectIDConverter
from pymongo import ReturnDocument
from pymongo.server_api import ServerApi
from bson import json_util, ObjectId
from flask_cors import CORS
import datetime as dt
from Schemas import ReadingSchemaPost

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
db = client.SoilCluster

#
# if 'light' not in db.list_collection_names():
#     db.create_collection("light",
#                          timeseries={'timeField': 'timestamp', 'metaField': 'sensorId', 'granularity': 'minutes'})
#

#def getTimeStamp():
 #   return dt.datetime.today().replace(microsecond=0)



app = Flask(__name__)

app.config['DEBUG'] = True
#making our API accessible by any IP
CORS(app)


@app.route('/add', methods=["POST"])
def add_data():
    # Get JSON Object
    read = request.json
    #Schema Validation
    error = ReadingSchemaPost().validate(read)
    if error:
        return error, 400

    #Write to DB and insert the lumen,humidity and collectionid
    try:
        addedId = db.results.insert_one(read).addedId
        read["_id"] = str(addedId)
        return jsonify(read)

    except Exception as error:
        return {"error": "some error happened"}, 500




#Get readings from DB
@app.route('/collection/<collection_id>', methods=["GET"])
def get_by_Id(collection_id):
    #Select from results DB using collection_id
    try:
        cursor = db.results.find({"collection_id": collection_id})
        read = list(cursor)
        for read in read:
            if "_id" in read:
                read["_id"] = str(read["_id"])

        # Return readings from query
        return jsonify(read)
    except Exception as e:
        print(e)
        return {"error": "some error happened"}, 501



@app.route('/addTest', methods=["POST"])
def add_data_test():
    # Get JSON Object
    read = request.json
    #Schema Validation
    error = ReadingSchemaPost().validate(read)
    if error:
        return error, 400

    #Write to DB and insert the lumen,humidity and collectionid
    try:
        return jsonify(read)

    except Exception as error:
        return {"error": "some error happened"}, 500



#Get readings from DB
@app.route('/collectionTest/<collection_id>', methods=["GET"])
def get_by_Id_test(collection_id):
    #Select from results DB using collection_id
    try:
      read = {

          "collection_id": collection_id,
          "lumen": 10.5,
          "humidity": 11
      }
      return jsonify(read)

      # Return readings from query
    except Exception as e:
        print(e)
        return {"error": "some error happened"}, 501






if __name__ == "__main__":
    app.run(port=5002)
