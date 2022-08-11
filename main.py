import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://luis:za0P2zKMKreo7QlO@pruebas.iysthfz.mongodb.net/?retryWrites=true&w=majority")
database = client.monedas_conmemorativas
collection = database["lista_intercambios"]

for x in collection.find():
  print(x)