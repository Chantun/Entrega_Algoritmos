class Superhero:
  def __init__(self, name: str, firstApareance: int, house: str, biography: str):
    self.name = name
    self.appearance = firstApareance
    self.house = house
    self.biography = biography
  
  def __str__(self):
    return f"""{self.name}:
    Aparicion: {self.appearance}
    Casa: {self.house}
    Biografia: {self.biography}"""

def order_by_name(hero):
  return hero.name
