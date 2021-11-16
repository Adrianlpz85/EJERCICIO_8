import json

def store(variable, archivo):
    variable = input("Variable: ")
    archivo = input("Nombre del archivo: ")

    json.dump(json.dumps(archivo), open(archivo, "w"))

def retrieve(archivo):
    return json.loads(json.load(archivo), open(archivo, "r"))