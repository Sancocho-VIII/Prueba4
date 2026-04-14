import random as rd
from datetime import datetime

def generar_nombre():
    nombre=['Paul', 'Utalio', 'Hermenegildo', 'Sancocho']
    personaje=rd.choice(nombre)
    return personaje
def generar_clase():
    clase = ['Paleador', 'Chud', 'Teramogger', 'GOAT']
    estilo=rd.choice(clase)
    return estilo
def generar_hp():
    hp= rd.randint(80,120)
    return hp
def mostrar_fecha():
    fecha = datetime.now()
    print(fecha)

print("=== GENERADOR DE AVENTURAS ===")
print(f"Fecha: {mostrar_fecha()}")
print("=== Heroes Generados ===")
for i in range(3):
    print(f"Heroe {i+1}: {generar_nombre()} / Clase: {generar_clase()} / HP: {generar_hp()}")