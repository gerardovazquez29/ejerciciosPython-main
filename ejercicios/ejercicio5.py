
#* Ejercicio 1: Crea un programa que imprima los números pares del 1 al 20 usando un bucle for.
for i in range(1,21):
    if i % 2 == 0:
        print(i)
#* Ejercicio 2: Crea una función que reciba una lista y un índice, 
#* y maneje los posibles errores al acceder al elemento.

def acceder_elemento(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return "Índice fuera de rango"
    except TypeError:
        return "El índice debe ser un número entero"
    except Exception as e:
        return f"Error inesperado: {e}" 
# Ejemplo de uso
lista = [1, 2, 3, 4, 5]
print(acceder_elemento(lista, 2))  # Salida: 3
print(acceder_elemento(lista, 10))  # Salida: Índice fuera de rango 
print(acceder_elemento(lista, "a"))  # Salida: El índice debe ser un número entero
print(acceder_elemento([1,2,3], 5)) # Salida: Índice fuera de rango


#* Ejercicio 3: Crea una clase CuentaBancaria con métodos para depositar, 
#* retirar y consultar saldo, manejando errores como fondos insuficientes.
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        try:
            if cantidad <= 0:
                raise ValueError("La cantidad a depositar debe ser mayor que cero.")
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}")
        except ValueError as e:
            print(f"Error al depositar: {e}")

    def retirar(self, cantidad):
        try:
            if 0 < cantidad <= self.saldo:
                self.saldo -= cantidad
                print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}")
            elif cantidad > self.saldo:
                raise ValueError("Fondos insuficientes.")
            else:
                raise ValueError("La cantidad a retirar debe ser mayor que cero.")
        except ValueError as e:
            print(f"Error al retirar: {e}")

    def consultar_saldo(self):
        return f"Saldo actual: {self.saldo}"
cuenta = CuentaBancaria("Juan", 1000)
cuenta.depositar(500)  # Saldo: 1500
cuenta.retirar(200)  # Saldo: 1300
print(cuenta.consultar_saldo())  # Saldo: 1300
cuenta.retirar(1500)  # Fondos insuficientes

