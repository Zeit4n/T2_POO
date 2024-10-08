#Importamos las clases definidas en los otros archivos además de librerías que utilizaremos
from personaje import Personaje
from equipamiento import Espada, Escudo
import random
import time

#Creamos los nombres de las espadas que los usuarios utilizarán en el juego
Espadas = [
    'Luz de Aurora',
    'Filo de la Tempestad',
    'Sombra del Destino',
    'Corte de Ébano',
    'Hoja de la Eternidad'
]

#Creamos los nombres de los escudos que los usuarios utilizarán en el juego
Escudos = [
    'Escudo del Guardián Eterno',
    'Barrera de la Fe',
    'Escudo de la Tempestad',
    'Defensor del Reino',
    'Escudo de las Sombras'
]

#Tomamos 3 nombres de espadas y escudos aleatorios
nombres_espadas = random.sample(Espadas,3)
nombres_escudos = random.sample(Escudos,3)

#Generamos 3 daños y afinidades aleatorios para espadas. Generamos además 3 defensas y durezas aleatorias para escudos
daños = random.sample(range(50,100),3)
defensas = random.sample(range(15,45),3)
afinidad = random.choices(range(0,4),k=3)
dureza = random.choices(range(0,4),k=3)

#Creamos una lista de 3 espadas y 3 escudos (listas de instancias de clase Espada y Escudo)
espadas = [Espada(nombres_espadas[i],daños[i],afinidad[i]) for i in range(3)]
escudos = [Escudo(nombres_escudos[i],defensas[i],dureza[i]) for i in range(3)]

#Inicia el juego solicitando nombre de ambos personajes
print("BIENVENIDO AL JUEGO 'GANAR O MORIR'")
p1 = input("Seleccione el nombre del jugador 1: ")
p2 = input("Seleccione el nombre del jugador 2: ")

#Cada jugador elige la espada y escudo que ocupará. Se crean los personajes con 1000 de HP
#y las espadas y escudos que eligieron. Sus velocidades son números aleatorios entre 10 y 20
for i in range(2):
    print(f"Seleccione una espada para jugador {i+1}: ")
    for j in range(3):
        print(f"{j+1})",espadas[j])
    elecc_espada = int(input(">>> "))
    print(f"Seleccione un escudo para jugador {i+1}: ")
    for j in range(3):
        print(f"{j+1})",escudos[j])
    elecc_escudo = int(input(">>> "))
    if i == 0:
        P1 = Personaje(p1, 1000, random.randint(10,20), espadas[elecc_espada-1], escudos[elecc_escudo-1])
    elif i == 1:
        P2 = Personaje(p2, 1000, random.randint(10,20), espadas[elecc_espada-1], escudos[elecc_escudo-1])

#Contador de turnos
t = 0

#Mientras ningún jugador esté muerto, los personajes se atacarán mutuamente
while P1.muerto == False and P2.muerto == False:
    t += 1
    print(f"TURNO {t}\n----------")
    #En cada turno comienza atacando quien tenga mayor velocidad
    if P1.velocidad >= P2.velocidad:
        vencedor = 2
        print(f"{P1.nombre} ataca a {P2.nombre} con {P1.espada.nombre}")
        ataque = P1.atacar()
        P2.recibir_daño(ataque)
        #Se evalúa si el jugador muere después de recibir el ataque del otro personaje
        if P2.muerto == True:
            #Se proclama el jugador 1 como vencedor en caso de que el jugador 2 muera.
            vencedor = 1
            break
        print(f"{P2.nombre} ataca a {P1.nombre} con {P2.espada.nombre}")
        ataque = P2.atacar()
        P1.recibir_daño(ataque)
        print(P1)
        print(P2)
        print("-----------------------------------------")
        time.sleep(3)

    elif P2.velocidad > P1.velocidad:
        vencedor = 1
        print(f"{P2.nombre} ataca a {P1.nombre} con {P2.espada.nombre}")
        ataque = P2.atacar()
        P1.recibir_daño(ataque)
        if P1.muerto == True:
            vencedor = 2
            break
        print(f"{P1.nombre} ataca a {P2.nombre} con {P1.espada.nombre}")
        ataque = P1.atacar()
        P2.recibir_daño(ataque)
        print(P1)
        print(P2)
        print("-----------------------------------------")
        time.sleep(3)

#Una vez se salga del ciclo while (un jugador muere), se imprime el vencedor del combate
if vencedor == 1:
    print(f"El jugador {P1.nombre} es el ganador.")
elif vencedor == 2:
    print(f"El jugador {P2.nombre} es el ganador.")


