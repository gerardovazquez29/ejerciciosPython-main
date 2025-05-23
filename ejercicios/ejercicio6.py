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

#* Agenda de contactos: Implementa búsqueda, añadir y eliminar contactos

class Contacto:
    """
    Clase que representa un contacto con nombre y teléfono.
    """
    def __init__(self, nombre, telefono):
        # Corrección: eliminar la coma que convertía nombre en tupla
        self.nombre = nombre
        self.telefono = telefono
        
    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}"


class Agenda:
    """
    Clase para gestionar una agenda de contactos.
    Permite añadir, buscar, eliminar y mostrar contactos.
    """
    def __init__(self):
        self.contactos = []

    def añadir_contacto(self, contacto):
        """
        Añade un contacto a la agenda si no existe.
        
        Args:
            contacto: Objeto de la clase Contacto
        
        Returns:
            bool: True si se añade, False si ya existe
        """
        # Verificar si ya existe un contacto con el mismo nombre
        if self.buscar_contacto(contacto.nombre):
            print(f"Ya existe un contacto con el nombre '{contacto.nombre}'")
            return False
        
        self.contactos.append(contacto)
        return True

    def buscar_contacto(self, nombre):
        """
        Busca un contacto por nombre.
        
        Args:
            nombre: Nombre del contacto a buscar
            
        Returns:
            Contacto: El contacto encontrado o None
        """
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto
        return None

    def eliminar_contacto(self, nombre):
        """
        Elimina un contacto de la agenda por su nombre.
        
        Args:
            nombre: Nombre del contacto a eliminar
            
        Returns:
            bool: True si se eliminó, False si no se encontró
        """
        contacto_previo = len(self.contactos)
        self.contactos = [c for c in self.contactos if c.nombre != nombre]
        
        if contacto_previo > len(self.contactos):
            print(f"Contacto '{nombre}' eliminado correctamente")
            return True
        else:
            print(f"No se encontró el contacto '{nombre}'")
            return False

    def mostrar_contactos(self):
        """
        Muestra todos los contactos de la agenda.
        """
        if not self.contactos:
            print("La agenda está vacía")
            return
        
        print("\n=== LISTA DE CONTACTOS ===")
        print("-------------------------")
        for i, contacto in enumerate(self.contactos, 1):
            print(f"{i}. {contacto}")
        print("-------------------------")
        print(f"Total: {len(self.contactos)} contactos")


def menu_agenda():
    """Función principal que muestra un menú interactivo para gestionar la agenda."""
    agenda = Agenda()
    
    # Pre-cargar algunos contactos de ejemplo
    agenda.añadir_contacto(Contacto("Juan", "123456789"))
    agenda.añadir_contacto(Contacto("Maria", "987654321"))
    
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Añadir contacto")
        print("2. Buscar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción (1-5): ")
        
        if opcion == "1":
            nombre = input("Introduzca el nombre: ")
            telefono = input("Introduzca el teléfono: ")
            nuevo_contacto = Contacto(nombre, telefono)
            agenda.añadir_contacto(nuevo_contacto)
            
        elif opcion == "2":
            nombre = input("Introduzca el nombre a buscar: ")
            contacto = agenda.buscar_contacto(nombre)
            if contacto:
                print(f"\nContacto encontrado: {contacto}")
            else:
                print(f"\nNo se encontró ningún contacto con el nombre '{nombre}'")
                
        elif opcion == "3":
            nombre = input("Introduzca el nombre del contacto a eliminar: ")
            agenda.eliminar_contacto(nombre)
            
        elif opcion == "4":
            agenda.mostrar_contactos()
            
        elif opcion == "5":
            print("¡Hasta pronto!")
            break
            
        else:
            print("Opción no válida. Intente de nuevo.")


# Para ejecutar la versión interactiva, descomenta la siguiente línea:
# menu_agenda()

# Ejemplo de uso básico (para mostrar funcionamiento)
if __name__ == "__main__":
    agenda = Agenda()
    print("=== Demostración de la agenda ===")
    
    # Añadir contactos
    contacto1 = Contacto("Juan", "123456789")
    contacto2 = Contacto("Maria", "987654321")
    agenda.añadir_contacto(contacto1)
    agenda.añadir_contacto(contacto2)
    
    # Mostrar contactos
    agenda.mostrar_contactos()
    
    # Buscar un contacto
    nombre_buscar = "Juan"
    print(f"\nBuscando contacto '{nombre_buscar}':")
    contacto_encontrado = agenda.buscar_contacto(nombre_buscar)
    if contacto_encontrado:
        print(f"Contacto encontrado: {contacto_encontrado}")
    else:
        print(f"Contacto '{nombre_buscar}' no encontrado.")
    
    # Eliminar un contacto
    print(f"\nEliminando contacto '{nombre_buscar}':")
    agenda.eliminar_contacto(nombre_buscar)
    
    # Mostrar contactos después de eliminar
    agenda.mostrar_contactos()