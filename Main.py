import pymongo as pymongo

client = pymongo.MongoClient("mongodb+srv://<username>:<password>@soilcluster.wz1jyhk.mongodb.net/?retryWrites=true&w=majority")
db = client.test