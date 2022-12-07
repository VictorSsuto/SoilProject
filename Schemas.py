from marshmallow import Schema, fields, validate

class ReadingSchemaPost(Schema):
    #deviceID = fields.String(required=False)
    #timeseries = fields.DateTime(required=True)
    lumen = fields.Float(required=True)
    humidity = fields.Float(required=True)
    devices = fields.Float(required=False)



# MONGODB_LINK = os.environ.get("MONGODB_LINK")
# MONGODB_USER = os.environ.get("MONGODB_USER")
# MONGODB_PASS = os.environ.get("MONGODB_PASS")
# import certifi
#
# client = pymongo.MongoClient(f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@{MONGODB_LINK}/?retryWrites=true&w=majority", tlsCAFile=ca, server_api=ServerApi('1'))