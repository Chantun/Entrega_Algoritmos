from list_ import List
class Jedi:

  def __init__(self, nombre: str, especie: str, maestros: List, color_sable: str):
    self.nombre = nombre
    self.especie = especie
    self.maestros = maestros
    self.color_sable = color_sable

  def __str__(self):
    return f"""{self.nombre}:
    Especie: {self.especie}
    Maestros: {self.maestros}
    Color de sable: {self.color_sable}"""

def order_by_nombre(jedi):
  return jedi.nombre

def order_by_especie(jedi):
  return jedi.especie
