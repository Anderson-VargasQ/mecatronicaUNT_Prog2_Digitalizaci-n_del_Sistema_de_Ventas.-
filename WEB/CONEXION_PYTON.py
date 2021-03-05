#pip install pymongo --user
#pip install dnspython --user
import pymongo

client = pymongo.MongoClient("mongodb+srv://grupo_hailpy:1a2b3c4d5e@proyectox.todpx.mongodb.net/Proyecto?retryWrites=true&w=majority")
db = client.test

try:
    print("MongoDB version is %s" % 
            client.server_info()['version'])
except pymongo.errors.OperationFailure as error:
    print(error)
    quit(1)

my_database = client.test
my_collection = my_database.Base

"""
#PARA INSERTAR UN SOLO DATO
my_collection.insert_one({
    '_id':'PH20G',
    'categoria': 'papel',
    'name':'elite',
    'precio_costo':'5',
    'precio_venta':'6',
    'utilidad':'1',
    'stock':'50',
    'reserva':'8',
    'stock_disp':'42'

})
"""
"""
#PARA INSERTAR VARIOS DATOS
my_collection.insert_many([
    {
        "_id": 12,
        "name": "pato",
        "calories": 295, "protein": 17,
        "fats": { "saturated": 5.0, "trans": 0.8 },
    },

    {
        "_id": 13,
        "name": "cabrito",
        "calories": 226, "protein": 9,
        "fats": { "saturated": 4.4, "trans": 0.5 },
    }
])

"""

"""
#Buscando un dato por código e imprime su nombre y otros parametros
codigo=input("codigo:")
my_cursor = my_collection.find({"_id": codigo})
for item in my_cursor:
    print(item["categoria"])
    print(item["name"])
    print(item["precio_venta"])
"""

#Devuelve los productos dentro de una categoria
"""
categoria=input("categoria:")

my_cursor = my_collection.find({"categoria": categoria})
for item in my_cursor:
    
    print(item["name"])
"""


"""
#Devuelve sólo aquellos documentos que cumplen criterios específicos
my_cursor = my_collection.find({
    "name": "PH20A"
})
"""
my_cursor = my_collection.find('categoria')
print(my_cursor)
"""
#Para cambiar parametros dentro de un dato
codigo=input("codigo:")
stock=input("Stock:")
my_collection.update_one(
    { "_id": codigo }, # query
    {
        "$set": {       # new data
            "stock": stock
            
        }
    }
)
"""











