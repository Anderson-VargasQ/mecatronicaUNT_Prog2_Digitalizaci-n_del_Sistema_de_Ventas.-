#pip install pymongo --user
#pip install dnspython --user
import pymongo
from editar_excel import list1
import random

client = pymongo.MongoClient("mongodb+srv://grupo_hailpy:1a2b3c4d5e@proyectox.todpx.mongodb.net/Proyecto?retryWrites=true&w=majority")
db = client.test

try:
    print("MongoDB version is %s" % 
            client.server_info()['version'])
except pymongo.errors.OperationFailure as error:
    print(error)
    quit(1)

my_database = client.test

my_collection = my_database.bases

#PARA INSERTAR UN SOLO DATO
for i in range(50):
    a=random.randrange(40,60,1)
    my_collection.insert_one({
        "_id": list1[i][2],
        "categoria": list1[i][0],
        "name": list1[i][1],
        "precio_costo": list1[i][3],
        "precio_venta": list1[i][4],
        "utilidad": list1[i][5],
        "stock": a,
        "reserva": 0,
        "stock_disp": a,

})
"""
#PARA INSERTAR VARIOS DATOS
my_collection.insert_many([
    {
        "_id": 69,
        "name": "andergei",
        "calories": 295, "protein": 17,
        "fats": { "saturated": 5.0, "trans": 0.8 },
    },
    {
        "_id": 44,
        "name": "alfredputo",
        "calories": 226, "protein": 9,
        "fats": { "saturated": 4.4, "trans": 0.5 },
    }
])


#Buscando un dato
my_cursor = my_collection.find()

for item in my_cursor:
    print(item["name"])

#Devuelve sólo aquellos documentos que cumplen criterios específicos
my_cursor = my_collection.find({
    "name": "pizza"
})

#Para cambiar parametros dentro de un dato
my_collection.update_one(
    { "name": "taco" }, # query
    {
        "$set": {       # new data
            "fiber": 3.95,
            "sugar": 0.9
        }
    }
)
"""
