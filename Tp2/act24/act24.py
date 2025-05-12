from stack import Stack
from personajes import Personaje
import os

personajesStack = Stack()

personajesStack.push(Personaje("Iron Man", 10))
personajesStack.push(Personaje("Captain America", 9))
personajesStack.push(Personaje("Thor", 9))
personajesStack.push(Personaje("Hulk", 8))
personajesStack.push(Personaje("Black Widow", 8))
personajesStack.push(Personaje("Hawkeye", 6))
personajesStack.push(Personaje("Spider-Man", 5))
personajesStack.push(Personaje("Doctor Strange", 4))
personajesStack.push(Personaje("Black Panther", 4))
personajesStack.push(Personaje("Scarlet Witch", 6))
personajesStack.push(Personaje("Vision", 4))
personajesStack.push(Personaje("Ant-Man", 4))
personajesStack.push(Personaje("Rocket Raccoon", 5))
personajesStack.push(Personaje("Groot", 4))
personajesStack.push(Personaje("Captain Marvel", 3))

def auxStack(stack:Stack):
    tempStack = Stack()
    newStack = Stack()
    for i in range(stack.size()):
        tempStack.push(stack.pop())
    for i in range(tempStack.size()):
        value = tempStack.pop()
        newStack.push(value)
        stack.push(value)
    return newStack

def buscarPosicion(stack: Stack, nombre: str):
    auxiliarStack = auxStack(stack)
    for i in range(auxiliarStack.size()):
        if nombre == auxiliarStack.pop().getNombre():
            return i + 1
    return -1

def mostrarPorPeliculas(stack: Stack, cantidad = 6):
    auxiliarStack = auxStack(stack)
    for i in range(auxiliarStack.size()):
        personaje = auxiliarStack.pop()
        if personaje.getPeliculas() >= cantidad:
            print(personaje)

def buscarPersonaje(stack: Stack, nombre: str):
    auxiliarStack = auxStack(stack)
    for i in range(auxiliarStack.size()):
        personaje = auxiliarStack.pop()
        if personaje.getNombre() == nombre:
            return personaje.getPeliculas()

def buscarIniciales(stack: Stack, iniciales: Stack):
    for letra in iniciales:
        auxiliarStack = auxStack(stack)
        print(f"Personajes cuyo nombre emieza con {letra}:")
        for i in range(auxiliarStack.size()):
            personaje = auxiliarStack.pop()
            if personaje.getNombre()[0].upper() == letra[0].upper():
                print(personaje)
        print()

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def menuPrincipal():
    limpiar_consola()
    print("1. Determinar la posicion de Rocket Raccoon y Groot")
    print("2. Buscar la posicion de otro personaje")
    print("3. Lista de personajes que aparecieron en mas de 5 peliculas")
    print("4. Filtrar personajes por cantidad de peliculas")
    print("5. Cantidad de peliculas en las que participo la Viuda Negra")
    print("6. Buscar cantidad de peliculas en las que aparecio un personaje")
    print("7. Mostrar todos los personajes cuyos nombre empiezan con C, D y G")
    print("8. Filtrar personajes por inicial")
    print("0. Salir")
    opcion = input("-> ")
    limpiar_consola()
    match opcion:
        case "1":
            print(f"Rocket Raccoon se encuentra en la posicion {buscarPosicion(personajesStack, "Rocket Raccoon")} de la lista")
            print()
            print(f"Groot se encuentra en la posicion {buscarPosicion(personajesStack, "Groot")} de la lista")
        case "2":
            personaje = input("Ingrese el personaje: ")
            pos = buscarPosicion(personajesStack, personaje)
            if pos == None:
                print(f"{personaje} no esta en la pila")
            else:
                print(f"{personaje} se encuentra en la posicion {pos} de la lista")
        case "3":
            print("Personajes que aparecieron en mas de 5 peliculas:")
            mostrarPorPeliculas(personajesStack)
        case "4":
            peliculas = input("Cantidad de peliculas: ")
            if peliculas.isdigit():
                print(f"Personajes que aparecieron en {peliculas} peliculas o mas:")
                mostrarPorPeliculas(personajesStack, int(peliculas))
            else:
                print("Opcion no valida.")
        case "5":
            print(f"Black Widow aparecio en {buscarPersonaje(personajesStack, "Black Widow")} peliculas")
        case "6":
            personaje = input("Ingrese el personaje: ")
            peliculas = buscarPersonaje(personajesStack, personaje)
            if peliculas == None:
                print(f"{personaje} no esta en la pila")
            else:
                print(f"{personaje} aparecio en {peliculas} peliculas")
        case "7":
            buscarIniciales(personajesStack, ["C", "D", "G"])
        case "8":
            buscarIniciales(personajesStack, [input("Ingrese la inicial: ")])
        case "0":
            print()
        case _:
            print("Opcion no valida.")
    if opcion != "0":
        print()
        input("ENTER para volver al menu principal")
        menuPrincipal()

menuPrincipal()
