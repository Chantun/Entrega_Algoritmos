from datetime import time

class Notificacion:

    def __init__(self, hora: time, app: str, mensaje: str):
        self.__hora = hora
        self.__app = app
        self.__mensaje = mensaje
    
    def __str__(self):
        return f"[{self.__hora}, {self.__app}, {self.__mensaje}]"

    def getHora(self):
        return self.__hora
    
    def getApp(self):
        return self.__app
    
    def getMensaje(self):
        return self.__mensaje
