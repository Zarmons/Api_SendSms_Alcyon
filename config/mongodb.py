import pymongo

MONGO_HOST="db-mongodb-nyc1-10694-770f0209.mongo.ondigitalocean.com"
MONGO_PUERTO= "27017"
MONGO_TIEMPO_FUERA= 100000

MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

try:

    client=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    client.server_info()
    print("exit")
    client.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido")
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo conexión")

