#* Calculadora simple: Crea un programa que pida dos números y una operación (+, -, *, /) y muestre el resultado.
def calculadora():
    num1 = int(input(("Introduce el primer número: ")))
    num2 = int(input(("Introduce el segundo número: ")))
    operacion = input("Introduce la operación (+, -, *, /): ")
    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        try:
            if num2 != 0:
                resultado = num1 / num2
            else:
                resultado = "Error: División por cero no permitida."
        except ZeroDivisionError:
            resultado = "Error: División por cero no permitida."
    else:
        resultado = "Error: Operación no válida."
    print("El resultado es:", resultado)
#calculadora()


#* Número par/impar: Pide un número al usuario y determina si es par o impar.
def par_impar():
    num = int(input("Introduce un número: "))
    if num % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
#par_impar()

#* Contador de vocales: Pide una palabra al usuario y cuenta cuántas vocales tiene.
def contador_vocales():
    palabra = input("Introduce una palabra: ")
    contador = 0
    for letra in palabra:
        if letra.lower() in "aeiouáéíóú":
            contador += 1
    print("La palabra tiene", contador, "vocales.")
#contador_vocales()

#* Adivina el número: Genera un número aleatorio entre 1 y 100 y 
#* da pistas al usuario si su intento es mayor o menor.
import random
def adivina_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    while True:
        intento = int(input("Adivina el número (entre 1 y 100): "))
        intentos += 1
        if intento < numero_secreto:
            print("El número es mayor.")
        elif intento > numero_secreto:
            print("El número es menor.")
        else:
            print("¡Felicidades! Adivinaste el número en", intentos, "intentos.")
            break
#adivina_numero()

#* funcion que filtra numeros pares de un array
def filtrar_pares(numeros):
    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)
    return pares
#print(filtrar_pares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


#*lista = [x for x in range(100) if x % 2 == 0]
#*print(lista)

# Dame un ejercicio para practicar recursión en Python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#print(factorial(5))  # Salida: 120


#*Contador de palabras: Cuenta cuántas veces aparece cada palabra en un texto
def contador_palabras(texto):
    palabras = texto.split()
    contador = {}
    for palabra in palabras:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1
    return contador
texto = "hola mundo hola"
#print(contador_palabras(texto))  # Salida: {'hola': 2, 'mundo': 1}
