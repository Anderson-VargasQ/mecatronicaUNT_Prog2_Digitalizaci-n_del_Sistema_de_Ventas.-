import pymongo


def crear_tupla_categorias():

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
    #Buscando un dato
    my_cursor = my_collection.find({})
    fila = []
    for item in my_cursor:
        fila.append(item["categoria"])
    return fila
