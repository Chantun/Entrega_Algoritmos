class Superheroe:

    def __init__(self, name: str, alias: str, real_name: str, short_bio: str, first_appearance: int, is_villain: bool):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.short_bio = short_bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):
        return (f"Nombre: {self.name}\n"
                f"Alias: {self.alias}\n"
                f"Nombre real: {self.real_name}\n"
                f"Biografía corta: {self.short_bio}\n"
                f"Primera aparición: {self.first_appearance}\n"
                f"¿Es villano?: {'Sí' if self.is_villain else 'No'}")
    
def order_by_name(superheroe):
    return superheroe.name

def order_by_real_name(superheroe):
    return str(superheroe.real_name)

def order_by_first_appearance(superheroe):
    return superheroe.first_appearance
