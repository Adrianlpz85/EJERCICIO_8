import json

lista_coche = []

while True:
    marca = input("Marca: ")
    if marca == "fin":
        break
    else:
        modelo = input("Modelo: ")
        combustible = input("Combustible: ")
        cilindrada = input("Cilindrada: ")
        linea= {}
        linea["Marca: "] = marca
        linea["Modelo: "] = modelo
        linea["Combustible: "] = combustible
        linea["Cilindrada: "] = cilindrada
        lista_coche.append(linea)

print("Lista coche:\n", lista_coche)

json.dump(json.dumps(lista_coche), open("coches.txt", "w"))

lista_coches = []

import persistencia_json

persistencia_json.store(lista_coches, "coches.txt")