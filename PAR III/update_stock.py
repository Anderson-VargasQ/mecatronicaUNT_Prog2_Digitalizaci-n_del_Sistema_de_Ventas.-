import pymongo

def update_stock(codigo_producto,stock,stock_disp):
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
    #Para cambiar parametros dentro de un dato
    my_collection.update_one(
        { "_id": codigo_producto }, # query
        {
            "$set": {       # new data
                "stock":stock,
                "stock_disp":stock_disp

            }
        }
    )