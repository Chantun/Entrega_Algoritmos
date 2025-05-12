class Heroe:

    def __init__(self, nombre: str, superheroe: str, genero: str):
        self.__nombre = nombre
        self.__superheroe = superheroe
        self.__genero = genero

    def __str__(self):
        return f"[{self.__nombre}, {self.__superheroe}, {self.__genero}]"

    def getNombre(self) -> str:
        return self.__nombre

    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def getSuperheroe(self) -> str:
        return self.__superheroe

    def setSuperheroe(self, superheroe: str):
        self.__superheroe = superheroe

    def getGenero(self) -> str:
        return self.__genero

    def setGenero(self, genero: str):
        self.__genero = genero
