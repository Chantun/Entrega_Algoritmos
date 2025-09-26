from list_ import List
from Jedi import *
from jedis_data import jedisData

jediList = List()

jediList.add_criterion('nombre', order_by_nombre)
jediList.add_criterion('especie', order_by_especie)

for jedi in jedisData:
  jediList.append(Jedi(jedi['nombre'], jedi['especie'], jedi['maestros'], jedi['color_sable']))

def showByMaestro(list, maestro):
  for element in list:
    if maestro in element.maestros:
      print(element)

def showByEspecie(list, value):
  for element in list:
    if element.especie == value:
      print(element)

def showByInitial(list, letter):
  for element in list:
    if element.nombre.startswith(letter):
      print(element)

def showByColor(list, value):
  for element in list:
    if value in element.color_sable:
      print(element)

def showByMultipleColors(list):
  for element in list:
    if len(element.color_sable) > 1:
      print(element)

# a. listado ordenado por nombre y por especie;

print('Listado ordenado por nombre:')
jediList.sort_by_criterion('nombre')
jediList.show()
print()

print('Listado ordenado por especie:')
jediList.sort_by_criterion('especie')
jediList.show()
print()

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;

index = jediList.search('Ahsoka Tano', 'nombre')
print(jediList[index])
print()

index = jediList.search('Kit Fisto', 'nombre')
print(jediList[index])
print()

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;

showByMaestro(jediList, 'Yoda')
print()
showByMaestro(jediList, 'Luke Skywalker')
print()

# d. mostrar los Jedi de especie humana y twi'lek;

showByEspecie(jediList, 'Humano')
print()
showByEspecie(jediList, "Twi'lek")
print()

# e. listar todos los Jedi que comienzan con A;

showByInitial(jediList, 'A')
print()

# f. mostrar los Jedi que usaron sable de luz de más de un color;

showByMultipleColors(jediList)
print()

# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;

showByColor(jediList, 'Amarillo')
print()
showByColor(jediList, 'Violeta')
print()

# h. indicar los nombre de los padawans de Qui-Gon Jinn y Mace Windu, si los tuvieron.

print(jediList[jediList.search('Qui-Gon Jinn', 'nombre')].maestros)
print(jediList[jediList.search('Mace Windu', 'nombre')].maestros)
