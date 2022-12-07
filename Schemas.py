from marshmallow import Schema, fields, validate

class ReadingSchemaPost(Schema):
    #deviceID = fields.String(required=False)
    #timeseries = fields.DateTime(required=True)
    lumen = fields.Float(required=True)
    humidity = fields.Float(required=True)
    devices = fields.Float(required=False)




