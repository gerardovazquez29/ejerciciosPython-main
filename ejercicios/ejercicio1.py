
#* bucles
"""
edad = int(input("dime cuantos años tienes: "))

if edad > 18:
    print(f"tu edad es: {edad} adelante puedes pasar")
elif edad == 18:
    print(f"tu edad es: {edad} esta bien pasa")
else:
    print(f"tu edad es: {edad} lo siento vete a tu casa")
"""

#* for
"""
frutas = ["manzana", "pera", "Durazno"]
for fruta in frutas:
    print(fruta)

for i in range(6):
    print(i)
"""
#* While
"""
numero = 10
while numero >= 1:
    print(numero)
    numero -= 1

numero = 1
while numero <= 10:
    print(numero)
    numero +=1
"""

#* funciones
def saludar(nombre):
    return f"Hola, {nombre}"
mensaje = saludar("Gerardo")
#print(mensaje)   # Hola, Gerardo

