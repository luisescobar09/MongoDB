from django.http import HttpResponse
from django.template import loader
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://luis:za0P2zKMKreo7QlO@pruebas.iysthfz.mongodb.net/?retryWrites=true&w=majority")
database = client.monedas_conmemorativas
collection = database["lista_intercambios"]

data = [ dict(i) for i in collection.find() ]

def index(request):
  template = loader.get_template('aplicacion.html')
  return HttpResponse(template.render( { 'data': data } ))