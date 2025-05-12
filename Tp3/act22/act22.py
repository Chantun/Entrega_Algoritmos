from heroes import Heroe
from queue_ import Queue
import os

heroesQueue = Queue()

heroesQueue.arrive(Heroe("Carol Danvers", "Capitana Marvel", "F"))
heroesQueue.arrive(Heroe("Scott Lang", "Ant-Man", "M"))
heroesQueue.arrive(Heroe("Stephen Strange", "Doctor Strange", "M"))
heroesQueue.arrive(Heroe("Steve Rogers", "Capitán América", "M"))
heroesQueue.arrive(Heroe("Sam Wilson", "Falcon", "M"))
heroesQueue.arrive(Heroe("Tony Stark", "Iron Man", "M"))
heroesQueue.arrive(Heroe("Natasha Romanoff", "Black Widow", "F"))
heroesQueue.arrive(Heroe("Bruce Banner", "Hulk", "M"))
heroesQueue.arrive(Heroe("Peter Parker", "Spider-Man", "M"))
heroesQueue.arrive(Heroe("T'Challa", "Black Panther", "M"))
heroesQueue.arrive(Heroe("Wanda Maximoff", "Scarlet Witch", "F"))
heroesQueue.arrive(Heroe("Clint Barton", "Hawkeye", "M"))

def getByAttribute(queue: Queue, value: str, nombre: bool = True):
    for i in range(queue.size()):
        if (queue.on_front().getNombre().upper() if nombre else queue.on_front().getSuperheroe().upper()) == value.upper():
            heroe = queue.attention()
            queue.arrive(heroe)
            return heroe
        else:
            queue.move_to_end()
    return Heroe(None, None, None)

def showByGenero(queue: Queue, gen: str, nombre: bool):
    for i in range(queue.size()):
        if queue.on_front().getGenero() == gen:
            heroe = queue.attention()
            if nombre == True:
                print(heroe.getNombre())
            else:
                print(heroe.getSuperheroe())
            queue.arrive(heroe)
        else:
            queue.move_to_end()

def showByLetter(queue: Queue, letter: str = "S"):
    for i in range(queue.size()):
        if queue.on_front().getNombre()[0].upper() == letter.upper():
            heroe = queue.attention()
            queue.arrive(heroe)
            print(heroe)
        else:
            queue.move_to_end()

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def menuPrincipal():
    limpiar_consola()
    print("1. Mostar cola")
    print("2. Determinar el nombre del personaje de la superhéroe Capitana Marvel")
    print("3. Mostrar los nombre de los superhéroes femeninos")
    print("4. Mostrar los nombres de los personajes masculinos")
    print("5. Determinar el nombre del superhéroe del personaje Scott Lang")
    print("6. Mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan con la letra S")
    print("7. Determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre de superhéroes.")
    print("0. Salir")
    opcion = input("-> ")
    limpiar_consola()
    match opcion:
        case "1":
            heroesQueue.show()
        case "2":
            print(f"El nombre de la Capitana Marvel es {getByAttribute(heroesQueue, "Capitana Marvel", False).getNombre()}")
        case "3":
            print("Superheroes femeninos:")
            showByGenero(heroesQueue, "F", False)
        case "4":
            print("Nombre de los hoeroes masculinos:")
            showByGenero(heroesQueue, "M", True)
        case "5":
            print(f"Scott Lang es {getByAttribute(heroesQueue, "Scott Lang").getSuperheroe()}")
        case "6":
            print("Heroes cuyo nombre comienza con S:")
            showByLetter(heroesQueue)
        case "7":
            carol = getByAttribute(heroesQueue, "Carol Danvers")
            if carol.getSuperheroe() != None:
                print(f"Carol Danvers esta en la cola y su nombre de superheroe es {carol.getSuperheroe()}")
            else:
                print("Carol Danvers no esta en la cola")
        case "0":
            print()
        case _:
            print("Opcion no valida.")

    if opcion != "0":
        print()
        input("ENTER para volver al menu principal")
        menuPrincipal()

menuPrincipal()
