from superhero import *
from list_ import List

superheroesList = List()

superheroesList.add_criterion('name', order_by_name)

def initializeHeroes(list):
  list.append(Superhero("Linterna Verde", 1940, "DC", "Miembro del Corps, usa un anillo para crear constructos de energía."))
  list.append(Superhero("Wolverine", 1974, "Marvel", "Mutante con factor curativo y garras de adamantium."))
  list.append(Superhero("Dr. Strange", 1963, "DC", "Hechicero supremo, experto en artes místicas."))
  list.append(Superhero("Flash", 1940, "DC", "Velocista que utiliza la Fuerza de la Velocidad para proteger Central City."))
  list.append(Superhero("Star-Lord", 1976, "Marvel", "Líder de los Guardianes de la Galaxia, aventurero espacial."))
  list.append(Superhero("Capitana Marvel", 1968, "Marvel", "Heroína con gran poder cósmico y ex-piloto militar."))
  list.append(Superhero("Mujer Maravilla", 1941, "DC", "Princesa amazona con fuerza sobrehumana y un lazo de la verdad."))
  list.append(Superhero("Batman", 1939, "DC", "Detective y vigilante que usa un traje y gadgets avanzados para luchar contra el crimen."))
  list.append(Superhero("Magneto", 1963, "Marvel", "Mutante capaz de controlar campos magnéticos."))
  list.append(Superhero("Spider-Man", 1962, "Marvel", "Adolescente con poderes arácnidos; trepa paredes y balancea por la ciudad."))
  list.append(Superhero("Iron Man", 1963, "Marvel", "Millonario que usa una armadura tecnológica para combatir el crimen."))
  list.append(Superhero("Black Panther", 1966, "Marvel", "Rey de Wakanda, guerrero con traje y tecnología avanzada."))

initializeHeroes(superheroesList)

def showByBiography(list, value):
  for element in list:
    if element.biography.lower().find(value) != -1:
      print(element)

def showByYear(list, year):
  for element in list:
    if element.appearance < year:
      print(f"{element.name}, {element.house}")

def showByInitial(list, initials):
  for letter in initials:
    for element in list:
      if element.name.lower().startswith(letter.lower()):
        print(element)
        print()

def countHouse(list, value):
  cont = 0
  for element in list:
    if element.house.lower() == value.lower():
      cont += 1
  return cont

# a. eliminar el nodo que contiene la información de Linterna Verde;

element = superheroesList.delete_value('Linterna Verde', 'name')
print(f"""Heroe eliminado:
{element}
""")

# b. mostrar el año de aparición de Wolverine;

index = superheroesList.search('Wolverine', 'name')
print(f"""Año de aparición de Wolverine: {superheroesList[index].appearance}
""")

# c. cambiar la casa de Dr. Strange a Marvel;

index = superheroesList.search('Dr. Strange', 'name')
superheroesList[index].house = 'Marvel'
print(f"""Casa de Dr. Strange cambiada:
{superheroesList[index]}
""")

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;

print('Superheroes con "traje" en su biografia:')
showByBiography(superheroesList, 'traje')
print()
print('Superheroes con "armadura" en su biografia:')
showByBiography(superheroesList, 'armadura')
print()

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;

print('Heroes cuya fecha de aparición es anterior a 1963:')
showByYear(superheroesList, 1963)
print()

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;

temp = ['Capitana Marvel', 'Mujer Maravilla']
for hero in temp:
  index = superheroesList.search(hero, 'name')
  element = superheroesList[index]
  print(f"""Casa de {element.name}: {element.house}""")
print()

# g. mostrar toda la información de Flash y Star-Lord;

temp = ['Flash', 'Star-Lord']
for hero in temp:
  index = superheroesList.search(hero, 'name')
  element = superheroesList[index]
  print(element)
  print()

# h. listar los superhéroes que comienzan con la letra B, M y S;

print('Heroes con iniciales B, M, S:')
showByInitial(superheroesList, ['B', 'M', 'S'])

# i. determinar cuántos superhéroes hay de cada casa de comic.

print(f"""Heroes de marvel: {countHouse(superheroesList, 'Marvel')}
Heroes de DC: {countHouse(superheroesList, 'DC')}""")
