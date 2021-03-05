import pymongo


def select_inventario(codigo_producto):

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
    my_cursor = my_collection.find({"_id":codigo_producto})

    for item in my_cursor:
        a=(item["name"])
        b=(item["precio_venta"])
        c=(item["stock"])
        d=(item["categoria"])
        e =(item['stock_disp'])
    fila = (a,b,c,d,e)
    return fila