
#* Crea un programa que calcule el área de un rectángulo (base x altura).
base = 5
altura = 5
area = base * altura 
#print(area)

def calcular_area_rectangulo(area,altura):
    return area * altura
area = calcular_area_rectangulo(5,3)
#print(f"La area de un  rectangulo es: {area} ")

base = int(input("ingresa la base del rectangulo: "))
altura = int(input("ingrsa la altura del rectangulo: "))
area = base * altura
#print(f"el area del rectangulo es: {area}")

#* Pide al usuario su edad y dile si puede votar (mayor de 18) o no.
"""
edad = int(input("Ingresa tu edad"))
if edad >= 18:
    print("Adelante puedes votar")
else:
    print("No puedes votar")
"""
#* Imprime los números pares del 0 al 10 usando un for.
"""
for num in range(11):
    if num % 2 == 0:
        print(num)

for i in range(0,11,2):
    print(i)
"""

#* Crea una lista de números y encuentra el mayor usando un bucle.
numeros = [1,2,23,4,5,16,7,78,9,10]
maximo = numeros[0]
for numero in numeros:
    if numero > maximo:
        maximo = numero
#print(f"el numero mas grande es: {maximo}")  # 78

#* Haz una función que reciba dos números y retorne su suma.
def suma(num1,num2):
    return num1 + num2
resultado = suma(5,6)
print(resultado)  #11 

