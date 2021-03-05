import pymongo

def insert_inventario(categoria_producto,nombre_producto,codigo_producto,precio_costo,precio_venta,utilidad,stock):


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

    my_collection.insert_one({
        "_id": codigo_producto,
        "categoria": categoria_producto,
        "name": nombre_producto,
        "precio_costo": precio_costo,
        "precio_venta": precio_venta,
        "utilidad": utilidad,
        "stock": stock,
        "reserva": 0,
        "stock_disp": stock,})