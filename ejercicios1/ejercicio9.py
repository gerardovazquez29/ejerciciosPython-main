

class Mago():
    def atacar(self):
        print("Ataque mágico")
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")
    def defender(self):
        print("Esconderse")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
    def defender(self):
        print("Bloqueo")

harypoter = Mago()
harcher = Arquero()
L = Samurai()

personajes = [harypoter, harcher, L]

print("\nAtaques de los personajes:")
for personaje in personajes:
    personaje.atacar()

print("\nDefensas de los personajes:")
for personaje in personajes:
    personaje.defender()

#    Ataques de los personajes:
# Ataque mágico
# Lanzamiento de flecha
# Ataque con katana

#      Defensas de los personajes:
# Escudo mágico
# Esconderse
# Bloqueo
