#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
# su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;[86]

#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;

#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return self.__elements.pop()
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)
    
personajes_mcu = Stack
personajes_mcu = {
    'Iron Man': {'nombre_real': 'Tony Stark', 'peliculas': 10},
    'Captain America': {'nombre_real': 'Steve Rogers', 'peliculas': 11},
    'Thor': {'nombre_real': 'Thor Odinson', 'peliculas': 8},
    'Black Widow': {'nombre_real': 'Natasha Romanoff', 'peliculas': 7},
    'Hulk': {'nombre_real': 'Bruce Banner', 'peliculas': 6},
    'Hawkeye': {'nombre_real': 'Clint Barton', 'peliculas': 6},
    'Spider-Man': {'nombre_real': 'Peter Parker', 'peliculas': 5},
    'Doctor Strange': {'nombre_real': 'Stephen Strange', 'peliculas': 4},
    'Black Panther': {'nombre_real': "T'Challa", 'peliculas': 4},
    'Ant-Man': {'nombre_real': 'Scott Lang', 'peliculas': 3},
    'Rocket Raccoon': {'nombre_real': 'Rocket', 'peliculas': 5},
    'Groot': {'nombre_real': 'Groot', 'peliculas': 5}
}


lista_personajes = list(personajes_mcu.keys())

def obtener_posicion(personaje):
    if personaje in lista_personajes:
        return lista_personajes.index(personaje) + 1
    else:
        return None

posicion_rocket = obtener_posicion('Rocket Raccoon')
posicion_groot = obtener_posicion('Groot')

for personaje, info in personajes_mcu.items():
    nombre_real = info['nombre_real']
    peliculas = info['peliculas']
    if peliculas > 5:
        print(f"{personaje} ({nombre_real}) participó en {peliculas} películas.")
        

peliculas_viuda_negra = personajes_mcu['Black Widow']['peliculas']
print(f"La Viuda Negra participó en {peliculas_viuda_negra} películas.")

personajes_cdg = []

for nombre_personaje in personajes_mcu:
    primera_letra = nombre_personaje[0]
    if primera_letra in ['C', 'D', 'G']:
        personajes_cdg.append(nombre_personaje)

print("Personajes que empiezan con 'C', 'D' o 'G':")
for personaje in personajes_cdg:
    print(personaje)
    

