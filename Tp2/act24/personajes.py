class Personaje:

    def __init__(self, nombre: str, peliculas: int):
        self.__nombre = nombre
        self.__peliculas = peliculas

    def __str__(self):
        return f"[{self.__nombre}, {self.__peliculas} peliculas]"
    
    def getNombre(self):
        return self.__nombre
    
    def getPeliculas(self):
        return self.__peliculas