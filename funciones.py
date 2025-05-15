
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