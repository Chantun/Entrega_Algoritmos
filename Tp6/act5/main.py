from graph import Graph
from stack import Stack


def get_path(path, objetive):
    stack = Stack()
    while path.size() > 0:
        node = path.pop()
        if node[0] == objetive:
            stack.push(node)
            objetive = node[2]
    return stack


def get_shortest(graph, array, objetive):
    current = graph.dijkstra(array[0])
    min = None
    shortest = array[0]
    while current.size() > 0 and min == None:
        node = current.pop()
        if node[0] == objetive:
            min = node[1]
    for i in range(1, len(array) - 1):
        current = graph.dijkstra(array[i])
        while current.size() > 0:
            node = current.pop()
            if node[0] == objetive:
                if node[1] < min:
                    min = node[1]
                    shortest = array[i]
                break
    return (shortest, min)


graph = Graph()

# Vertices

graph.insert_vertex("Parrot", "PC")
graph.insert_vertex("Manjaro", "PC")
graph.insert_vertex("Fedora", "PC")
graph.insert_vertex("Mint", "PC")
graph.insert_vertex("Ubuntu", "PC")
graph.insert_vertex("Arch", "Notebook")
graph.insert_vertex("Red Hat", "Notebook")
graph.insert_vertex("Debian", "Notebook")
graph.insert_vertex("MongoDB", "Servidor")
graph.insert_vertex("Guarani", "Servidor")
graph.insert_vertex("Switch 1", "Switch")
graph.insert_vertex("Switch 2", "Switch")
graph.insert_vertex("Router 1", "Router")
graph.insert_vertex("Router 2", "Router")
graph.insert_vertex("Router 3", "Router")
graph.insert_vertex("Impresora", "Impresora")

# Aristas

graph.insert_edge("Debian", "Switch 1", 17)
graph.insert_edge("Ubuntu", "Switch 1", 18)
graph.insert_edge("Impresora", "Switch 1", 22)
graph.insert_edge("Mint", "Switch 1", 80)
graph.insert_edge("Router 1", "Switch 1", 29)

graph.insert_edge("Router 2", "Router 1", 37)
graph.insert_edge("Router 3", "Router 1", 43)

graph.insert_edge("Red Hat", "Router 2", 25)
graph.insert_edge("Guarani", "Router 2", 9)
graph.insert_edge("Router 3", "Router 2", 50)

graph.insert_edge("Router 3", "Switch 2", 61)

graph.insert_edge("Manjaro", "Switch 2", 40)
graph.insert_edge("Parrot", "Switch 2", 12)
graph.insert_edge("MongoDB", "Switch 2", 5)
graph.insert_edge("Arch", "Switch 2", 56)
graph.insert_edge("Fedora", "Switch 2", 3)

# B. Barrido en profundiad partiendo de las 3 notebooks.

print("Barrido en profundiad partiendo de las 3 notebooks: \n")
graph.deep_sweep("Red Hat")
print()
graph.deep_sweep("Debian")
print()
graph.deep_sweep("Arch")
print()

# B. Barrido en amplitud partiendo de las 3 notebooks.

print("Barrido en amplitud partiendo de las 3 notebooks: \n")
graph.amplitude_sweep("Red Hat")
print()
graph.amplitude_sweep("Debian")
print()
graph.amplitude_sweep("Arch")
print()

# C. Encontrar el camino más corto para enviar a imprimir un documento desde la pc: Manjaro, Red Hat, Fedora hasta la impresora.

print("Camino más corto para enviar a imprimir un documento desde la pc Manjaro:")
path = graph.dijkstra("Manjaro")
get_path(path, "Impresora").show()
print()

print("Camino más corto para enviar a imprimir un documento desde la pc Red Hat:")
path = graph.dijkstra("Red Hat")
get_path(path, "Impresora").show()
print()

print("Camino más corto para enviar a imprimir un documento desde la pc Fedora:")
path = graph.dijkstra("Fedora")
get_path(path, "Impresora").show()
print()

# D. Encontrar el árbol de expansión mínima.

tree = graph.kruskal("Impresora")
print("Arbol de expansion minima:")
print(tree)
print()

# E. Determinar desde que pc (no notebook) es el camino más corto hasta el servidor “Guaraní”.

shortestPath = get_shortest(
    graph, ["Manjaro", "Parrot", "Fedora", "Mint", "Ubuntu"], "Guarani"
)
print(
    f"El camino mas corto desde un pc hasta el servidor Guarani es el de {shortestPath[0]} con un peso de {shortestPath[1]}"
)
print()

# F. Indicar desde que computadora del switch 01 es el camino más corto al servidor “MongoDB”.

shortestPath = get_shortest(graph, ["Debian", "Ubuntu", "Mint"], "MongoDB")
print(
    f"El camino mas corto desde un pc del Switch 01 hasta el servidor MongoDB es el de {shortestPath[0]} con un peso de {shortestPath[1]}"
)
print()

# G. cambiar la conexión de la impresora al router 02 y vuelva a resolver el punto B.

graph.delete_edge("Impresora", "Switch 1", "value")
graph.insert_edge("Impresora", "Router 2", 22)

print("Barrido en profundiad partiendo de las 3 notebooks: \n")
graph.deep_sweep("Red Hat")
print()
graph.deep_sweep("Debian")
print()
graph.deep_sweep("Arch")
print()

print("Barrido en amplitud partiendo de las 3 notebooks: \n")
graph.amplitude_sweep("Red Hat")
print()
graph.amplitude_sweep("Debian")
print()
graph.amplitude_sweep("Arch")
