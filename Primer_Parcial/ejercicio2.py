from super_heroe_class import *
from super_heroes_data import superheroes
from list_ import List
from queue_ import Queue
import os

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

superheroesList = List()

superheroesList.add_criterion('name', order_by_name)
superheroesList.add_criterion('real_name', order_by_real_name)
superheroesList.add_criterion('first_appearance', order_by_first_appearance)

def list_villains(personajes : List):
    for personaje in personajes:
        if personaje.is_villain:
            print(personaje.name)

def list_by_initial(personajes: List, char: str):
    for personaje in personajes:
        if personaje.name[:len(char)] == char:
            print(personaje.name)

def list_by_bio(personajes: List, bio : str):
    for personaje in personajes:
        if bio in personaje.short_bio:
            print(f'''{personaje.name}:
Short_bio: {personaje.short_bio}
''')

def queue_villain(personajes: List):
    queue = Queue()
    for personaje in personajes:
        if personaje.is_villain:
            queue.arrive(personaje)
    return queue

def list_by_year(personajes: Queue, year: int):
    for _ in range(personajes.size()):
        personaje = personajes.attention()
        if personaje.first_appearance < 1980:
            print(personaje.name)

for i in range(114):
    superheroesList.append(Superheroe(superheroes[i]['name'], superheroes[i]['alias'], superheroes[i]['real_name'], superheroes[i]['short_bio'], superheroes[i]['first_appearance'], superheroes[i]['is_villain']))

def menu():
    while True:
        print("""
Menú de opciones:
1. Listado ordenado por nombre de los personajes
2. Posición de The Thing y Rocket Raccoon
3. Listar todos los villanos
4. Villanos en cola y los que aparecieron antes de 1980
5. Listar superhéroes que comienzan con Bl, G, My, W
6. Listado ordenado por nombre real
7. Listado ordenado por fecha de aparición
8. Modificar nombre real de Ant Man a Scott Lang
9. Mostrar personajes con 'time-traveling' o 'suit' en la bio
10. Eliminar a Electro y Baron Zemo y mostrar su info
0. Salir
""")
        opcion = input("Seleccione una opción: ")
        clear_terminal()
        match opcion:
            case "1":
                superheroesList.sort_by_criterion('name')
                for superheroe in superheroesList:
                    print(superheroe.name)
            case "2":
                print(f"""The Thing está en la posición {superheroesList.search('The Thing', 'name')}
Rocket Raccoon está en la posición {superheroesList.search('Rocket Raccoon', 'name')}""")
            case "3":
                print('Villanos:')
                list_villains(superheroesList)
            case "4":
                villainQueue = queue_villain(superheroesList)
                print('''Cola de villanos creada'

'Villanos que aparecieron antes de 1980:''')
                list_by_year(villainQueue, 1980)
            case "5":
                for initials in ['Bl', 'G', 'My', 'W']:
                    print()
                    print(f'Personajes que inician con {initials}:')
                    list_by_initial(superheroesList, initials)
            case "6":
                superheroesList.sort_by_criterion('real_name')
                for superheroe in superheroesList:
                    print(f'{superheroe.name}, {superheroe.real_name}')
            case "7":
                superheroesList.sort_by_criterion('first_appearance')
                for superheroe in superheroesList:
                    print(f'{superheroe.name}, {superheroe.first_appearance}')
            case "8":
                AntManIndex = superheroesList.search('Ant Man', 'name')
                superheroesList[AntManIndex].real_name = 'Scott Lang'
                print(f'''Nombre real modificado con exito.

{superheroesList[AntManIndex].name}, {superheroesList[AntManIndex].real_name}''')
            case "9":
                print('Personajes con "time-traveling" en su bio:')
                list_by_bio(superheroesList, 'time-traveling')
                print('Personajes con "suit" en su bio:')
                list_by_bio(superheroesList, 'suit')
            case "10":
                Electro = superheroesList.delete_value('Electro', 'name')
                Baron_Zemo = superheroesList.delete_value('Baron Zemo', 'name')
                print('Personajes eliminados de la lista:')
                print()
                print(Electro)
                print()
                print(Baron_Zemo)
            case "0":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")
        print()
        input('Precione enter para continuar')
        clear_terminal()

menu()
