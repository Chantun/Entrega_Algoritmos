from tree import BinaryTree
from data import pokemons
from collections import Counter


def initTree(tree, value):
    for pokemon in pokemons:
        tree.insert(pokemon[value], pokemon)


def show_by_key(tree, key, value):
    def __search(root):
        if root is not None:
            __search(root.left)
            if value in root.other_values[key]:
                print(root.other_values["name"])
            __search(root.right)

    if tree.root is not None:
        __search(tree.root)


def get_types(tree):
    def __get_types(root):
        if root is not None:
            __get_types(root.left)
            for type in root.value:
                types.append(type)
            __get_types(root.right)

    types = []
    __get_types(tree.root)
    return Counter(types)


def get_by_key(tree, key, value):
    nodes = []

    def __count(root):
        if root is not None:
            __count(root.left)
            if root.other_values[key] == value:
                nodes.append(root.value)
            __count(root.right)

    __count(tree.root)
    return nodes


nameTree = BinaryTree()
numberTree = BinaryTree()
typeTree = BinaryTree()

initTree(nameTree, "name")
initTree(numberTree, "number")
initTree(typeTree, "types")

# Mostrar datos

node = numberTree.search(479)
print(f"Pokemon {node.value}: {node.other_values}\n")

print('Buscando a Magnezone con la busqueda de proximidad "ne":')
nameTree.proximity_search("ne")
node = nameTree.search("Magnezone")
print(f"\nPokemon {node.value}: {node.other_values}")

# mostrar por tipos

print("\nPokemones de tipo fantasma:")
show_by_key(typeTree, "types", "fantasma")
print("\nPokemones de tipo fuego:")
show_by_key(typeTree, "types", "fuego")
print("\nPokemones de tipo acero:")
show_by_key(typeTree, "types", "acero")
print("\nPokemones de tipo electrico:")
show_by_key(typeTree, "types", "electrico")

# listados

print("\nListado ascendente por número:")
numberTree.in_order()
print("\nListado ascendente por nombre:")
nameTree.in_order()
print("\nListado por nivel por nombre:")
nameTree.by_level()

# mostrar por debilidad

print("\nPokemones debiles a Jolteon:")
show_by_key(typeTree, "weaknesses", "electrico")
print("\nPokemones debiles a Lycanroc:")
show_by_key(typeTree, "weaknesses", "roca")
print("\nPokemones debiles a Tyrantrum:")
show_by_key(typeTree, "weaknesses", "roca")
show_by_key(typeTree, "weaknesses", "dragon")

# mostrar tipos y cantidad

print("\nListado de disntos tipos y sus cantidades:")
types = get_types(typeTree)
for type, n in types.items():
    print(f"{type}: {n}")

# pokemons con megaevolucion

print("\nPokemones con megaevolucion:")
megas = get_by_key(nameTree, "mega", True)
for mega in megas:
    print(mega)
print(f"\nLa cantidad total de pokemones con mega es: {len(megas)}")

# pokemons con forma gigamax

print("\nPokemones con forma gigamax:")
gigamaxs = get_by_key(nameTree, "gigamax", True)
for giga in gigamaxs:
    print(giga)
print(f"\nLa cantidad total de pokemones con forma gigamax es: {len(gigamaxs)}")
