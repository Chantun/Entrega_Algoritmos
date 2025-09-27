from data import criaturas
from tree import BinaryTree

creatureTree = BinaryTree()

for creature in criaturas:
    creatureTree.insert(creature["name"], creature)

# a. listado inorden de las criaturas y quienes la derrotaron;

creatureTree.in_order()
print()

# b. se debe permitir cargar una breve descripción sobre cada criatura;

creatureTree.modify_param(
    "Hidra de Lerna",
    "description",
    "La Hidra de Lerna era un monstruo acuático de la mitología griega con forma de serpiente o dragón, famoso por tener múltiples cabezas (según las versiones, entre 5 y 100). Cada vez que una de sus cabezas era cortada, dos nuevas crecían en su lugar, lo que la hacía extremadamente difícil de derrotar. Además, su aliento y su sangre eran venenosos. Fue vencida por Heracles en su segundo trabajo, quien logró derrotarla cauterizando los cuellos para impedir que volvieran a crecer.",
)
element = creatureTree.search("Hidra de Lerna")
print(f"{element.value}, {element.other_values['description']}")
print()

# c. mostrar toda la información de la criatura Talos;

element = creatureTree.search("Talos")
print(f"{element.value}, {element.other_values}")
print()

# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;

print("Los 3 héroes o dioses que derrotaron mayor cantidad de criaturas son:")
hunters = creatureTree.count_hunters(3)
for tuple in hunters:
    print(f"{tuple[0]}: {tuple[1]}")
print()

# e. listar las criaturas derrotadas por Heracles;

print("Criaturas derrotadas por Heracles:")
creatureTree.in_order_by_param("defeated_by", "Heracles")
print()

# f. listar las criaturas que no han sido derrotadas;

print("Criaturas que no han sido derrotadas:")
creatureTree.in_order_by_param("defeated_by", None)
print()

# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;

creatureTree.modify_param("Toro de Creta", "captured_by", "Heracles")
element = creatureTree.search("Toro de Creta")
print(f"{element.value}, {element.other_values}")
creatureTree.modify_param("Cierva de Cerinea", "captured_by", "Heracles")
element = creatureTree.search("Cierva de Cerinea")
print(f"{element.value}, {element.other_values}")
creatureTree.modify_param("Jabalí de Erimanto", "captured_by", "Heracles")
element = creatureTree.search("Jabalí de Erimanto")
print(f"{element.value}, {element.other_values}")
print()

# i. se debe permitir búsquedas por coincidencia;

creatureTree.proximity_search("de")
print()

# j. eliminar al Basilisco y a las Sirenas;

print(
    f"""Critaturas eliminadas:
{creatureTree.delete('Basilisco')[0]}
{creatureTree.delete('Sirenas')[0]}
"""
)

# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;

creatureTree.modify_param("Aves del Estínfalo", "defeated_by", "Heracles")
element = creatureTree.search("Aves del Estínfalo")
print(f"{element.value}, {element.other_values}")
print()

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;

element = list(creatureTree.delete("Ladón"))
element[0] = "Dragón Ladón"
element[1]["name"] = "Dragón Ladón"
creatureTree.insert(element[0], element[1])
element = creatureTree.search("Dragón Ladón")
print(f"{element.value}, {element.other_values}")
print()

# m. realizar un listado por nivel del árbol;

print("Listado por nivel:")
creatureTree.by_level()
print()

# n. muestre las criaturas capturadas por Heracles.

print("Criaturas capturadas por Heracles:")
creatureTree.in_order_by_param("captured_by", "Heracles")
