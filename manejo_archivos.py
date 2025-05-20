
#* Escritura
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, mundo!\n")
    archivo.write("Este es un archivo de texto.\n")
    archivo.write("Adiós, mundo!\n")
#* Lectura
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
#* Lectura línea por línea
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip()) 
#* Escritura en modo append
with open("archivo.txt", "a") as archivo:
    archivo.write("Esta línea se agrega al final del archivo.\n")
#* Lectura de un archivo CSV
