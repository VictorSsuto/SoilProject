import pymongo as pymongo
from flask import Flask, request, jsonify
from pymongo.server_api import ServerApi
from flask_cors import CORS
import datetime as dt
from Schemas import ReadingSchemaPost
import EmulatedData as em

# loading private connection information from environment variables
from dotenv import load_dotenv

load_dotenv()
import os

MONGODB_LINK = os.environ.get("MONGODB_LINK")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")
import certifi

ca = certifi.where()

client = pymongo.MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}/?retryWrites=true&w=majority",
                             tlsCAFile=ca, server_api=ServerApi('1'))

# connecting to mongodb
db = client.SoilCluster

if 'SoilTimeseries' not in db.list_collection_names():
    db.create_collection("SoilTimeseries",
                         timeseries={'timeField': 'timestamp', 'metaField': 'deviceId', 'granularity': 'hours'})


def gettimestamp():
    return dt.datetime.today().replace(microsecond=0)


app = Flask(__name__)

app.config['DEBUG'] = True
# making our API accessible by any IP
CORS(app)


@app.route('/add', methods=["POST"])
def add_data():
    # Get JSON Object
    read = request.json
    # Schema Validation
    error = ReadingSchemaPost().validate(read)
    if error:
        return error, 400

    # Write to DB and insert the lumen,humidity and collectionid
    # try:
    addedId = db.results.insert_one(read).inserted_id
    read["_id"] = str(addedId)

    return jsonify(read)


# Get readings from DB
@app.route('/collection/<collection_id>', methods=["GET"])
def get_by_Id(collection_id):
    # Select from results DB using collection_id
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


@app.route("/device/<int:deviceID>/devices", methods=["POST"])
def add_motion_value(deviceID):
    error = ReadingSchemaPost().validate(request.json)
    if error:
        return error, 400

    data = request.json
    data.update({"timestamp": gettimestamp(), "deviceID": deviceID})

    db.motion.insert_one(data)

    data["_id"] = str(data["_id"])
    data["timestamp"] = data["timestamp"].strftime("%Y-%m-%dT%H:%M:%S")
    return data


# Get all
@app.route("/devices", methods=["GET"])
def get_All():
    query = em.db.results.find()
    deviceList = {}

    for x in query:
        deviceList = {'devices': x}

    data = list(em.db.SoilTimeseries.aggregate([

        {
            '$match': deviceList
        }, {
            '$group': {
                '_id': 'none',
                'avgHumidity': {
                    '$avg': '$humidity'
                },
                'avgLumen': {
                    '$avg': '$lumen'
                },
                'Levels': {
                    '$push': {
                        'timestamp': '$timestamp',
                        'lumen': '$lumen',
                        'humidity': '$humidity'
                    }
                }
            }
        }
    ]))
    return data



# Get by ID

@app.route("/devices/<int:deviceID>", methods=["GET"])
def get_By_Id(deviceID):
    start = request.args.get("start")
    end = request.args.get("end")

    deviceList = {"id": deviceID}
    if start is None and end is not None:
        try:
            end = dt.datetime.strptime(end, "%Y-%m-%dT%H:%M:%S")
        except Exception as e:
            return {"error": "timestamp not following format %Y-%m-%dT%H:%M:%S"}, 400

        deviceList.update({"timestamp": {"$lte": end}})

    elif end is None and start is not None:
        try:
            start = dt.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
        except Exception as e:
            return {"error": "timestamp not following format %Y-%m-%dT%H:%M:%S"}, 400

        deviceList.update({"timestamp": {"$gte": start}})
    elif start is not None and end is not None:
        try:
            start = dt.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
            end = dt.datetime.strptime(end, "%Y-%m-%dT%H:%M:%S")

        except Exception as e:
            return {"error": "timestamp not following format %Y-%m-%dT%H:%M:%S"}, 400

        # Aggregation pipeline
        deviceList.update({"timestamp": {"$gte": start, "$lte": end}})

    data = list(em.db.SoilTimeseries.aggregate([
        {
            '$match': deviceList
        }, {
            '$group': {
                '_id': '$deviceID',
                'avgHumidity': {
                    '$avg': '$humidity'
                },
                'avgLumen': {
                    '$avg': '$lumen'
                },
                'Levels': {
                    '$push': {
                        'timestamp': '$timestamp',
                        'humidity': '$humidity',
                        'lumen': '$lumen'

                    }
                }
            }
        }
    ]))

    if data:
        data = data[0]
        if "_id" in data:
            del data["_id"]
            data.update({"id": deviceID})

        for device in data['Levels']:
            device["timestamp"] = device["timestamp"].strftime("%Y-%m-%dT%H:%M:%S")

        return data
    else:
        return {"error": "ID does not exist"}, 404


if __name__ == "__main__":
    app.run(port=5002)
