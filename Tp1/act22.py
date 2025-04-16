mochilaJedi = [
    "holocrón Jedi",
    "provisiones",
    "módulo de comunicación",
    "sable de luz",
    "kit de reparación",
    "ropa extra",
    "cristales kyber",
    "medidor de fuerza",
    "mapa estelar",
]

def usarLaFuerza(buscado, mochila, contador=1):
    print()
    print("Usando la fuerza en la mochila sacaste:")
    if len(mochila) == 0:
        return f"Nada, la mochila está vacia y no hay sable de luz."
    else:
        if mochila[0].lower() == buscado.lower():
            return f"{buscado}, al {contador}° intento."
        else:
            print(mochila[0])
            return usarLaFuerza(buscado, mochila[1:], contador + 1)

print(usarLaFuerza("sable de luz", mochilaJedi))
