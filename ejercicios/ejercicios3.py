"""

#* Ejercicio 1: Suma de números pares en una lista
#* Descripción: Escribe una función que reciba una lista de números y 
#* devuelva la suma de todos los números pares.
#suma_pares([1, 2, 3, 4, 5, 6])  # Debe retornar 12 (2 + 4 + 6)
lista = [1,2,3,4,5,6]

def suma_pares(lista):
    return sum(num for num in lista if num % 2 == 0)
resultado = suma_pares(lista)
print(f"la suma de los pares es : {resultado}") #12
            
#* Ejercicio 2: Contar vocales en una cadena
#* Descripción: Crea una función que cuente cuántas vocales (a, e, i, o, u) hay en una cadena.   
cadena = "Hola Mundo"# Debe retornar 4 (o, a, u, o)
def contar_vocal(cadena):
    return sum(1 for letra in cadena if letra.lower() in "aeiou")
print(contar_vocal(cadena))

#* Ejercicio 3: Encontrar el número más grande en una lista
#*Descripción: Implementa una función que encuentre el número más 
#* grande en una lista (sin usar max()).
maximo =[3, 8, 12, 10, 5]  # Debe retornar 10
def encontrar_maximo(lista):
    maximo = lista[0]
    for num in lista:
        if num > maximo:
            maximo = num
    return maximo
resultado = encontrar_maximo(maximo)
print(f"el maximo numero es: {resultado}")   

#*Ejercicio 4: Invertir una cadena
#*Descripción: Escribe una función que invierta una cadena (sin usar [::-1] o reversed).
cadena = "Hola mundo"
invertido = ""
for caracter in cadena:
    invertido = caracter + invertido
print(invertido)

invertida = cadena[::-1]
print(invertida)



#* jercicio 5: Verificar palíndromo
#* Descripción: Una palabra es palíndromo si se lee igual al derecho y al revés
#*  (ej: "reconocer"). 
#* Haz una función que devuelva True si es palíndromo.

es_palindromo = "Anita lava la tina"
if es_palindromo.lower().replace(" ","") == es_palindromo.lower().replace(" ", "")[::-1]:
    print(f"{es_palindromo} Es un palindromo valido!")
else:
    print(f"{es_palindromo} No es un palindromo valido!")  


def palindromo(palabra):
    palabra = palabra.lower().replace(" ","")
    return palabra == palabra[::-1]

texto = input("Ingresa una palabra o frase: ")
if palindromo(texto):
    print(f" {texto} es un palindromo")
else:
    print(f" {texto} no es un palindromo")
    

#*Ejercicio 6: Factorial de un número
#*Descripción: Escribe una función recursiva o iterativa que calcule el factorial de 
#* un número entero positivo.
#*factorial(5)  # Debe retornar 120 (5 * 4 * 3 * 2 * 1)
def factorial(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1,n + 1):
        resultado *= i
    return resultado
print(factorial(5))
"""
#* Ejercicio 7: Filtrar palabras por longitud
#* Descripción: Dada una lista de palabras, devuelve una lista con las palabras que tienen 
#* más de n letras.
#*Ejemplo:
lista_palabras = ["hola", "python", "sol", "programación"]  
# Debe retornar ["python", "programación"]

def filtrar_palabras(palabras, longitud):
    return [palabra for palabra in palabras if len(palabra) > longitud]
resultado = filtrar_palabras(lista_palabras, 4)
print(resultado) # ["python", "programación"]


