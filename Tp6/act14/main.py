from graph import Graph
from stack import Stack


def total_weight(string):
    aristas = string.split(";")
    total = 0
    for arista in aristas:
        parts = arista.split("-")
        weight = int(parts[-1])
        total += weight
    return total


def get_path(path, objetive):
    stack = Stack()
    while path.size() > 0:
        node = path.pop()
        if node[0] == objetive:
            stack.push(node)
            objetive = node[2]
    return stack


def get_meters(path):
    while path.size() != 1:
        path.pop()
    return path.pop()[1]


graph = Graph()

graph.insert_vertex("cocina")
graph.insert_vertex("comedor")
graph.insert_vertex("cochera")
graph.insert_vertex("quincho")
graph.insert_vertex("baño 1")
graph.insert_vertex("baño 2")
graph.insert_vertex("habitacion 1")
graph.insert_vertex("habitacion 2")
graph.insert_vertex("sala de estar")
graph.insert_vertex("terraza")
graph.insert_vertex("patio")

graph.insert_edge("cocina", "comedor", 5)
graph.insert_edge("cocina", "baño 1", 8)
graph.insert_edge("cocina", "habitacion 1", 8)
graph.insert_edge("comedor", "sala de estar", 3)
graph.insert_edge("comedor", "habitacion 2", 8)
graph.insert_edge("cochera", "sala de estar", 6)
graph.insert_edge("cochera", "habitacion 1", 3)
graph.insert_edge("cochera", "patio", 7)
graph.insert_edge("quincho", "patio", 12)
graph.insert_edge("quincho", "baño 2", 4)
graph.insert_edge("quincho", "terraza", 6)
graph.insert_edge("baño 1", "habitacion 2", 3)
graph.insert_edge("baño 1", "habitacion 1", 4)
graph.insert_edge("baño 2", "terraza", 5)
graph.insert_edge("baño 2", "habitacion 2", 6)
graph.insert_edge("sala de estar", "patio", 7)
graph.insert_edge("terraza", "quincho", 9)

# C. Obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes.

tree = graph.kruskal("patio")
print("Arbol de expansion minima:")
print(tree)
print(
    f"\nPara conectar todos los ambientes, seran necesarios {total_weight(tree)} metros de cable\n"
)

# D. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

path = graph.dijkstra("habitacion 1")
singlePath = get_path(path, "sala de estar")
print("El camino mas corto desde la habitación 1 hasta la sala de estar es:\n")
singlePath.show()
print(f"\nPor lo tanto seran necesarios {get_meters(singlePath)} metros de cable")
