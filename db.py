from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://rcastro86:gSNQLK4BFv4iOyd5@castroproyecto.4ivau6p.mongodb.net/?retryWrites=true&w=majority"
def conexion():
    try:
        # Create a new client and connect to the server
        client = MongoClient(uri, server_api=ServerApi('1'))
        db=client['Libro']
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        return db
    except Exception as e:
        print("Errro al conectar al MongoDb",e)
conexion()