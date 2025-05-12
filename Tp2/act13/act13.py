from IronMan import IronMan
from stack import Stack
import os

ironManStack = Stack()
ironManStack.push(IronMan("Mark I", "Iron Man", "Destruido"))
ironManStack.push(IronMan("Mark II", "Iron Man", "Impecable"))
ironManStack.push(IronMan("Mark III", "Iron Man", "Dañado"))
ironManStack.push(IronMan("Mark IV", "Iron Man 2", "Impecable"))
ironManStack.push(IronMan("Mark V", "Iron Man 2", "Dañado"))
ironManStack.push(IronMan("Mark VI", "Iron Man 2", "Impecable"))
ironManStack.push(IronMan("Mark VI", "The Avengers", "Dañado"))
ironManStack.push(IronMan("Mark VII", "The Avengers", "Impecable"))
ironManStack.push(IronMan("Mark XLII", "Iron Man 3", "Dañado"))
ironManStack.push(IronMan("Mark XLIII", "Iron Man 3", "Destruido"))
ironManStack.push(IronMan("Mark I - XLII", "Iron Man 3", "Destruido"))
ironManStack.push(IronMan("Mark XLIII", "Avengers: Age of Ultron", "Dañado"))
ironManStack.push(IronMan("Mark XLIV (Hulkbuster)", "Avengers: Age of Ultron", "Impecable"))
ironManStack.push(IronMan("Mark XLV", "Avengers: Age of Ultron", "Dañado"))
ironManStack.push(IronMan("Mark XLVI", "Capitan America: Civil War", "Dañado"))
ironManStack.push(IronMan("Mark XLVII", "Spider-Man: Homecoming", "Impecable"))
ironManStack.push(IronMan("Mark L", "Avengers: Infinity War", "Dañado"))

def auxStack(stack: Stack):
    newStack = Stack()
    tempStack = Stack()

    for i in range(stack.size()):
        tempStack.push(stack.pop())

    for i in range(tempStack.size()):
        item = tempStack.pop()
        newStack.push(item)
        stack.push(item)
    return newStack

def hulkbuster(stack: Stack):
    hulkbusterStack = Stack()
    for i in range (stack.size()):
        traje = stack.pop()
        if traje.getModelo() == "Mark XLIV (Hulkbuster)":
            hulkbusterStack.push(traje.getPelicula())
    return hulkbusterStack

def mostarDañados(stack: Stack):
    auxiliarStack = auxStack(stack)
    print("Trajes dañados:")
    for i in range(stack.size()):
        traje = auxiliarStack.pop()
        if traje.getEstado() == "Dañado":
            print(traje)

def mostrarPorPelicula(stack: Stack, pelicula: str):
    auxiliarStack = auxStack(stack)
    for i in range(stack.size()):
        traje = auxiliarStack.pop()
        if traje.getPelicula() == pelicula:
            print(traje)

def eliminarDestruidos(stack: Stack):
    tempStack = Stack()
    print("Trajes eliminados por estar destruidos:")
    for i in range(stack.size()):
        traje = stack.pop()
        if traje.getEstado() == "Destruido":
            print(traje)
        else:
            tempStack.push(traje)
    for i in range(tempStack.size()):
        stack.push(tempStack.pop())

def añadirTraje(stack: Stack, modelo: str, pelicula: str, estado: str):
    auxiliarStack = auxStack(stack)
    cargado = False
    for i in range(auxiliarStack.size()):
        trajeAux = auxiliarStack.pop()
        if modelo == trajeAux.getModelo() and pelicula == trajeAux.getPelicula():
            print("El traje ya esta cargado")
            cargado = True
            break
    if cargado != True:
        stack.push(IronMan(modelo, pelicula, estado))

def añadirTrajeManual(stack: Stack):
    añadirTraje(stack, input("Modelo del nuevo traje: "), input("Pelicula en la que aparecio: "), input("Estado en el que quedo: "))

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def menuPrincipal():
    limpiar_consola()
    print("1. Verificar si el modelo ”Mark XLIV (Hulkbuster)” esta en la pila")
    print("2. Mostrar trajes dañados")
    print("3. Eliminar de la pila los modelos destruidos")
    print("4. Agregar modelo ”Mark LXXXV” a la pila")
    print("5. Cargar nuevo modelo a la pila")
    print("6. Mostrar los trajes usados en las películas “Spider-Man: Homecoming” y “Capitan America: Civil War”")
    print("7. Mostrar todos los trajes de la pila")
    print("0. Salir")
    opcion = input("-> ")
    limpiar_consola()
    match opcion:
        case "1":
            hulkbusterMovies = hulkbuster(auxStack(ironManStack))
            if hulkbusterMovies.size() > 0:
                print("Peliculas donde aparecio el traje Mark XLIV (Hulkbuster):")
                hulkbusterMovies.show()
            else:
                print("El traje Mark XLIV (Hulkbuster) no aparecio en ninguna pelicula")
        case "2":
            mostarDañados(ironManStack)
        case "3":
            eliminarDestruidos(ironManStack)
        case "4":
            print("Mark LXXXV añadio.")
            añadirTraje(ironManStack, "Mark LXXXV", "Avengers: Endgame", "Destruido")
        case "5":
            añadirTrajeManual(ironManStack)
        case "6":
            print("Trajes de la pelicula Spider-Man: Homecoming:")
            mostrarPorPelicula(ironManStack, "Spider-Man: Homecoming")
            print()
            print("Trajes de la pelicula Capitan America: Civil War:")
            mostrarPorPelicula(ironManStack, "Capitan America: Civil War")
        case "7":
            ironManStack.show()
        case "0":
            print()
        case _:
            print("Opcion no valida.")

    if opcion != "0":
        print()
        input("ENTER para volver al menu principal")
        menuPrincipal()

menuPrincipal()

