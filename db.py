from pymongo import MongoClient


# Подключение к MongoDB
client = MongoClient('localhost', 27017)
db = client['Documents']

collection = db['Employees']
collection_contracts = db['Contracts']
collection_partners = db['Partners']