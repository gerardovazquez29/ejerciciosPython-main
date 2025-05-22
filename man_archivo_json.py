
import json

#* Escritura de un archivo JSON
datos = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
with open("datos.json", "w") as archivo_json:
    json.dump(datos, archivo_json, indent=4)
    # indent=4 es para que el archivo JSON sea más legible
    # Si no se pone, el JSON estará en una sola línea
    # Se puede usar también el parámetro sort_keys=True para ordenar las claves alfabéticamente
    # json.dump(datos, archivo_json, indent=4, sort_keys=True)

#* Lectura de un archivo JSON
with open("datos.json", "r") as archivo_json:
    datos_leidos = json.load(archivo_json)
    print(datos_leidos)
    # {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

