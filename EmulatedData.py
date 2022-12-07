import pymongo
import datetime as dt
import random
from time import sleep
import certifi
import os



#load the environment
from dotenv import load_dotenv
from pymongo.server_api import ServerApi

load_dotenv()
MONGODB_LINK = os.environ.get("MONGODB_LINK")
MONGODB_USER = os.environ.get("MONGODB_USER")
MONGODB_PASS = os.environ.get("MONGODB_PASS")

#find the certificate
ca = certifi.where()

client = pymongo.MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}/?retryWrites=true&w=majority", tlsCAFile=ca, server_api=ServerApi('1'))

#connecting to mongodb
db = client.SoilCluster

#If the sensor is on...
sensor = True

#Time series
if 'SoilTimeseries' not in db.list_collection_names():
    db.create_collection("SoilTimeseries",
                         timeseries={'timeField': 'timestamp', 'metaField': 'deviceId', 'granularity': 'hours'})





if __name__ == "__main__":
    while sensor:
        humidity = random.randint(0, 100)
        lumen = random.randint(0, 100)

        db.SoilTimeseries.insert_one({

            'id': 1,
            'timestamp': dt.datetime.now(),
            'humidity': humidity,
            'lumen': lumen
        })
        db.SoilTimeseries.insert_one({

            'id': 2,
            'timestamp': dt.datetime.now(),
            'humidity': humidity,
            'lumen': lumen
        })
        db.SoilTimeseries.insert_one({

            'id': 3,
            'timestamp': dt.datetime.now(),
            'humidity': humidity,
            'lumen': lumen
        })
        db.SoilTimeseries.insert_one({

            'id': 4,
            'timestamp': dt.datetime.now(),
            'humidity': humidity,
            'lumen': lumen
        })
        sleep(2000)
