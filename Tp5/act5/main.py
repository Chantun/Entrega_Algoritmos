from tree import BinaryTree
from super_heroes_data import superheroes

superheroTree = BinaryTree()

for hero in superheroes:
  superheroTree.insert(hero['name'], hero)

# b. listar los villanos ordenados alfabéticamente;

print('Villanos en orden:')
superheroTree.villain_in_order()
print()

# c. mostrar todos los superhéroes que empiezan con C;

print('Superhéroes que empiezan con C:')
superheroTree.show_by_initial('C')
print()

# d. determinar cuántos superhéroes hay el árbol;

print(f"Cantidad de superheroes: {superheroTree.count_heroes()}")
print()

# e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para encontrarlo en el árbol y modificar su nombre;

print('Modificando a Dr Strange:')
superheroTree.proximity_search('Dr')
node = superheroTree.search('Dr Strannnnnge')
node.value = 'Dr Strange'
node.other_values['name'] = 'Sr Strange'
print(f"{node.value}, {node.other_values}")
superheroTree.delete('Dr Strannnnnge')
superheroTree.insert(node.value, node.other_values)
print()

# f. listar los superhéroes ordenados de manera descendente;

print('Listado de manera descendente:')
superheroTree.post_order()
print()

# g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a los villanos, luego resolver las siguiente tareas:
  
villainTree = BinaryTree()
heroTree = BinaryTree()
superheroTree.divide_tree(heroTree, villainTree)

  # I. determinar cuántos nodos tiene cada árbol;

print('Nodos del arbol de heroes: ', heroTree.count_nodes())
print('Nodos del arbol de villanos: ', villainTree.count_nodes())
print()

  # II. realizar un barrido ordenado alfabéticamente de cada árbol.

print('Barrido alfabetico de cada arbol:')
heroTree.in_order()
print()
villainTree.in_order()
