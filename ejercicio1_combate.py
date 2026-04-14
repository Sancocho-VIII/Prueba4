def calcular_dano(ataque, defensa):
    dano_calculado = ataque - defensa
    if dano_calculado <0:
        dano_calculado=0
    return dano_calculado
def aplicar_dano(hp_actual, dano):
    hp_nueva = hp_actual-dano
    if hp_nueva <0:
        hp_nueva=0
    return hp_nueva
def mostrar_estado(nombre, hp, hp_max=100):
    print("="*20)
    print("Nombre    HP/HPMAX")
    print(f"{nombre}    {hp}/{hp_max}")
    print("="*20)
def realizar_ataque(atacante, defensor, dano):
    print(f"{atacante} ataca a {defensor} por {dano} de dano!")
hp_heroe = 100
hp_enemigo = 50

mostrar_estado("heroe", hp_heroe)
mostrar_estado("enemigo", hp_enemigo)
dano_hecho=calcular_dano(25, 10)
print(dano_hecho)
realizar_ataque("heroe", "enemigo", dano_hecho)
hp_enemigo=aplicar_dano(hp_enemigo, dano_hecho)
mostrar_estado("enemigo", hp_enemigo)
realizar_ataque("heroe", "enemigo", dano_hecho)
hp_enemigo=aplicar_dano(hp_enemigo, dano_hecho)
mostrar_estado("enemigo", hp_enemigo)