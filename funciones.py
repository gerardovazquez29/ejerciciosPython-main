
#* fnciones con argumentos 
#* Argumentos posisionales y por clave
def describe_persona(nombre, edad, ciudad="Desconocida"):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")
describe_persona("Juan", 30)
describe_persona(edad=25, nombre="Ana")

#* funciones lambda
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Salida: 25

#* funciones integradas
numeros = [1, 2, 3, 4]
suma = sum(numeros)  # sum es una función integrada
longitud = len(numeros)  # len es otra función integrada
print(f"Suma: {suma}, Longitud: {longitud}")


#* decoradores
def mi_decorador(func):
    def wrapper():
        print("Antes de llamar a la función")
        func()
        print("Después de llamar a la función")
    return wrapper

@mi_decorador
def saludar():
    print("Hola!")

saludar()
# Salida:
# Antes de llamar a la función
# Hola!
# Después de llamar a la función

# Explicación: Los decoradores modifican/complementan el comportamiento de funciones

#* Crea un decorador que mida el tiempo de ejecución de una función.

import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecucion: {fin - inicio} segundos")
        return resultado
    return wrapper
@medir_tiempo
def calcular_suma(n):
    suma = 0
    for i in range(n):
        suma += i
        time.sleep(0.1)
    return suma
resultado = calcular_suma(10)
print(f"Suma: {resultado}")

#* Crea una función que reciba una lista y devuelva un diccionario 
#* con el conteo de cada elemento único.

def contar_elementos(lista):
    conteo = {}
    for elemento in lista:
        conteo[elemento] = conteo.get(elemento, 0) + 1
    return conteo

print(contar_elementos(["a", "b", "a", "c", "b", "a"]))
# Salida: {'a': 3, 'b': 2, 'c': 1}


#* map
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16]

#* filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4]

#* reduce
from functools import reduce
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # Salida: 10

#* zip
