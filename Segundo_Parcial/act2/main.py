from graph import Graph
from stack import Stack


def expansion_tree(graph, value):
    tree = graph.kruskal(value)
    print(tree)
    aristas = tree.split(";")
    peso_total = 0

    for item in aristas:
        if "-" in item:
            _, _, peso = item.split("-")
            peso = int(peso)
            peso_total += peso
    return peso_total


def max_weight(graph):
    max = 0
    vertices = []
    for vertex in graph:
        for edge in vertex.edges:
            if edge.weight > max:
                max = edge.weight
                vertices = [vertex.value]
            elif edge.weight == max:
                vertices.append(vertex.value)
    return max, vertices


def get_path(path, objetive):
    stack = Stack()
    while path.size() > 0:
        node = path.pop()
        if node[0] == objetive:
            stack.push(node)
            objetive = node[2]
    return stack


def get_by_weight(graph, weight):
    values = []

    for vertex in graph:
        for edge in vertex.edges:
            if edge.weight == weight:
                values.append(vertex.value)
                break
    return values


graph = Graph()

graph.insert_vertex("Luke Skywalker")
graph.insert_vertex("Darth Vader")
graph.insert_vertex("Yoda")
graph.insert_vertex("Boba Fett")
graph.insert_vertex("C_3PO")
graph.insert_vertex("Leia")
graph.insert_vertex("Rey")
graph.insert_vertex("Kylo Ren")
graph.insert_vertex("Chewbacca")
graph.insert_vertex("Han Solo")
graph.insert_vertex("R2_D2")
graph.insert_vertex("BB_8")

graph.insert_edge("Luke Skywalker", "Leia", 4)
graph.insert_edge("Luke Skywalker", "Han Solo", 4)
graph.insert_edge("Luke Skywalker", "Darth Vader", 3)
graph.insert_edge("Luke Skywalker", "Yoda", 2)
graph.insert_edge("Luke Skywalker", "Chewbacca", 4)
graph.insert_edge("Leia", "Han Solo", 4)
graph.insert_edge("Leia", "Chewbacca", 4)
graph.insert_edge("Han Solo", "Chewbacca", 4)
graph.insert_edge("R2_D2", "C_3PO", 9)
graph.insert_edge("R2_D2", "Luke Skywalker", 4)
graph.insert_edge("C_3PO", "Luke Skywalker", 4)
graph.insert_edge("C_3PO", "Leia", 4)
graph.insert_edge("C_3PO", "Han Solo", 4)
graph.insert_edge("Darth Vader", "Leia", 2)
graph.insert_edge("Darth Vader", "Yoda", 1)
graph.insert_edge("Darth Vader", "Chewbacca", 1)
graph.insert_edge("Yoda", "R2_D2", 2)
graph.insert_edge("Yoda", "C_3PO", 2)
graph.insert_edge("Boba Fett", "Darth Vader", 1)
graph.insert_edge("Boba Fett", "Han Solo", 1)
graph.insert_edge("Boba Fett", "Chewbacca", 1)
graph.insert_edge("Rey", "Kylo Ren", 3)
graph.insert_edge("Rey", "Leia", 2)
graph.insert_edge("Rey", "Luke Skywalker", 2)
graph.insert_edge("Rey", "BB_8", 3)
graph.insert_edge("Rey", "Chewbacca", 2)
graph.insert_edge("Kylo Ren", "Leia", 2)
graph.insert_edge("Kylo Ren", "Luke Skywalker", 1)

# arboles de expancion

print("Arbol de expancion minima desde C-3PO:")
total = expansion_tree(graph, "C_3PO")
print(f"Peso total del arbol: {total}\n")

print("Arbol de expancion minima desde Yoda:")
total = expansion_tree(graph, "Yoda")
print(f"Peso total del arbol: {total}\n")

print("Arbol de expancion minima desde Leia:")
total = expansion_tree(graph, "Leia")
print(f"Peso total del arbol: {total}\n")

# episodios compartidos

episode, characters = max_weight(graph)
print(f"Número máximo de episodio que comparten dos personajes: {episode}")
print("Y los personajes son:")
for character in characters:
    print(character)

# caminos mas cortos

path = graph.dijkstra("C_3PO")
path = get_path(path, "R2_D2")
print("\nCamino mas corto desde C-3PO hasta R2-D2:")
path.show()

path = graph.dijkstra("Yoda")
path = get_path(path, "Darth Vader")
print("\nCamino mas corto desde Yoda hasta Darth Vader:")
path.show()

# aparecio en 9 capitulos

print(f"\nPersonajes que aparecieron en 9 capitulos: {get_by_weight(graph, 9)}")
