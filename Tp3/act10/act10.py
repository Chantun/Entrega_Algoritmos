from notificaciones import Notificacion
from queue_ import  Queue
from stack import Stack
from datetime import time
import os

notifQueue = Queue()

notifQueue.arrive(Notificacion(time(10, 15), "WhatsApp", "Hola, ¿cómo estás?"))
notifQueue.arrive(Notificacion(time(11, 50), "Facebook", "Tienes un nuevo recuerdo para ver."))
notifQueue.arrive(Notificacion(time(12, 30), "Twitter", "Trending: #PythonRocks"))
notifQueue.arrive(Notificacion(time(13, 10), "Instagram", "¡Nueva historia de tu amigo!"))
notifQueue.arrive(Notificacion(time(8, 5), "WhatsApp", "Nuevo mensaje en el grupo."))
notifQueue.arrive(Notificacion(time(15, 45), "Gmail", "Confirmación de tu pedido."))
notifQueue.arrive(Notificacion(time(16, 20), "Twitter", "Últimas noticias del mundo."))
notifQueue.arrive(Notificacion(time(17, 5), "Instagram", "Nuevo mensaje directo."))
notifQueue.arrive(Notificacion(time(9, 35), "WhatsApp", "¿Vamos al cine hoy?"))
notifQueue.arrive(Notificacion(time(14, 25), "Instagram", "Revisa las nuevas fotos que subieron."))
notifQueue.arrive(Notificacion(time(19, 15), "Instagram", "Publicación destacada de la semana."))
notifQueue.arrive(Notificacion(time(21, 50), "Facebook", "¡Nuevo evento cerca de ti!"))
notifQueue.arrive(Notificacion(time(6, 45), "WhatsApp", "Buen día :)"))
notifQueue.arrive(Notificacion(time(11, 43), "Twitter", "Python 3.12 ya está disponible."))
notifQueue.arrive(Notificacion(time(12, 15), "WhatsApp", "No olvides traer los documentos."))
notifQueue.arrive(Notificacion(time(18, 30), "Gmail", "Reunión cancelada."))
notifQueue.arrive(Notificacion(time(22, 5), "Instagram", "Tu foto fue comentada."))
notifQueue.arrive(Notificacion(time(13, 25), "Twitter", "Aprende Python desde cero."))
notifQueue.arrive(Notificacion(time(20, 10), "Facebook", "Un amigo reaccionó a tu publicación."))
notifQueue.arrive(Notificacion(time(9, 0), "WhatsApp", "Nos vemos en la facultad."))

def eliminarPorApp(queue: Queue, app = "Facebook"):
    for i in range(queue.size()):
        if queue.on_front().getApp() == app:
            queue.attention()
        else:
            queue.move_to_end()

def mostrarAppMsj(queue: Queue, app: str = "Twitter", msj: str = "Python"):
		for i in range(queue.size()):
				notif = queue.attention()
				if notif.getApp().upper().find(app.upper()) != -1 and notif.getMensaje().upper().find(msj.upper()) != -1:
						print(notif)
				queue.arrive(notif)

def pilaHrs(queue: Queue, hrs1: time = time(11, 43), hrs2: time = time(15, 57)):
    stack = Stack()
    for i in range(queue.size()):
        if hrs1 < queue.on_front().getHora() < hrs2:
            notif = queue.attention()
            stack.push(notif)
            queue.arrive(notif)
        else:
            queue.move_to_end()
    return stack

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def setTime():
    while True:
        aux = True
        hora_str = input()
        if ":" not in hora_str:
            print("Formato de hora no válido. Debe ser 'hh:mm'.")
            aux = False
            continue
        partes = hora_str.split(":")
        if len(partes) != 2 or not partes[0].isdigit() or not partes[1].isdigit():
            print("Formato de hora no válido. Debe ser 'hh:mm'.")
            aux = False
            continue
        horas = int(partes[0])
        minutos = int(partes[1])
        if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
            print("Hora fuera de rango. Las horas deben estar entre 0 y 23, y los minutos entre 0 y 59.")
            aux = False
            continue
        if aux == True:
            return time(horas, minutos)

def menuPrincipal():
    limpiar_consola()
    print("1. Mostrar notificaciones")
    print("2. Eliminar notificaciones de facebook")
    print("3. Eliminar notificaciones de una app")
    print("4. Mostrar mensajes de twitter que mecionen a Python")
    print("5. Filtrar mensajes por app y mensaje")
    print("6. Almacenar los mensajes enviados entre las 11:43 y las 15:57 en una pila")
    print("7. Almacenar los mensajes por hora en una pila")
    print("0. Salir")
    opcion = input("-> ")
    limpiar_consola()
    match opcion:
        case "1":
            notifQueue.show()
        case "2":
            eliminarPorApp(notifQueue)
            print("Eliminadas las notificaciones de facebook")
        case "3":
            app = input("Ingrese la app: ")
            eliminarPorApp(notifQueue, app)
            print(f"Eliminadas las notificaciones de {app}")
        case "4":
            print("Mensajes de Twitter que mencionan a Python:")
            mostrarAppMsj(notifQueue)
        case "5":
            app = input("Ingrese la app (Puede quedar en blanco): ")
            msj = input("Ingrese una palabra para filtrar los mensajes (Puede quedar en blanco):")
            limpiar_consola()
            print("Mensajes filtrados:")
            mostrarAppMsj(notifQueue, app, msj)
        case "6":
            print("Notificaciones entre las 11:43 y las 15:57:")
            hrsStack = pilaHrs(notifQueue)
            hrsStack.show()
        case "7":
            print("Hora inicial:")
            hrs1 = setTime()
            print()
            print("Hora final:")
            hrs2 = setTime()
            limpiar_consola()
            print(f"Notificaciones entre las {hrs1} y las {hrs2}:")
            hrsStack = pilaHrs(notifQueue, hrs1, hrs2)
            hrsStack.show()
        case "0":
            print()
        case _:
            print("Opcion no valida.")

    if opcion != "0":
        print()
        input("ENTER para volver al menu principal")
        menuPrincipal()

menuPrincipal()
