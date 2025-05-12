class IronMan:

    def __init__(self, modelo: str, pelicula: str, estado: str):
        self.__modelo = modelo
        self.__pelicula = pelicula
        self.__estado = estado
    
    def __str__(self):
        return f"[{self.__modelo}, {self.__pelicula}, {self.__estado}]"
    
    def setModelo(self, value: str):
        self.__modelo = value

    def getModelo(self):
        return self.__modelo
    
    def setPelicula(self, value: str):
        self.__pelicula = value
    
    def getPelicula(self):
        return self.__pelicula
    
    def setEstado(self, value: str):
        self.__estado = value
    
    def getEstado(self):
        return self.__estado
