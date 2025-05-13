"""
*  
**  
***  
```*  
**Solución paso a paso**:  
1. Usa un bucle para cada fila.  
2. En cada iteración, imprime asteriscos igual al número de fila actual.  
 **Conclusión**: La práctica constante con problemas **gradualmente más difíciles** 
 es la clave. Si te atas en un problema, vuelve a lo básico y desglósalo. ¡Tú puedes! 
¿Quieres que te sugiera más ejercicios específicos? 
"""
def print_stars(n):
    for i in range(1, n + 1):
        print("*" * i)
print_stars(3)  # Cambia el número para más filas

"""
1. Suma de Dos Números
Enunciado: Dados dos números, retorna su suma.
Pista: Usa una función que tome 2 parámetros.
Desafío extra: Valida si los inputs son números
""" 
def suma_dos_numeros():
    numero_1 = int(input("Ingresa el primer numero: "))
    numero_2 = int(input("Ingresa el segundo numero: "))
    suma = numero_1 + numero_2
    return suma
#*print(suma_dos_numeros())  # Cambia los números para probar

#* contar vocales en una cadena

def contar_vocales(cadena):
    return [ letra for letra in cadena if letra.lower()in 'aeiou']
resultado =contar_vocales("Hola Mundo Python es genial")
print(resultado)

