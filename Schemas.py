from marshmallow import Schema, fields, validate

class ReadingSchemaPost(Schema):
    collection_id = fields.String(required=True)
    #timeseries = fields.DateTime(required=True)
    lumen = fields.Float(required=True)
    humidity = fields.Float(required=True)



