

buscar = 5
for numero in range(5):
    print(numero)
    if  numero == buscar:
     print("encontrado", buscar)
    break
else:
    print("no encontre el numero buscado:(")

for char in "Hola":
   print(char)


n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
suma = n1 + n2
resta = n1  - n2
multi = n1 * n2
div = n1 / n2

mensaje = f"Para los numeros {n1} y {n2}, El resultado de la suma es  {suma}, El resultado de la resta es {resta}, El resultado de la multiplicacion es {multi}, El resultado de la division es {div} "
print(mensaje)



websites = ["nytimes.com", "lemonde.fr", "economist.com" ]

french = [website for website in websites if website.count(".fr") == 1]
print(french)

numbers = ["+43 5753335", "+44 0051128", "+33 1218817"]

uk_numbers = [num for num in numbers if num.count("+44") == 1]

print(uk_numbers)


