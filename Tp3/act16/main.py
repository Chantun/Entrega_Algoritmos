from heap import HeapMax


def priorityParser(n: int):
    match n:
        case 1:
            return "Empleado"
        case 2:
            return "IT staff"
        case 3:
            return "Gerente"


documents = HeapMax()

# a. cargue tres documentos de empleados (cada documento se representa solamente conun nombre).
documents.arrive("curriculum.docx", 1)
documents.arrive("sueldos.xls", 1)
documents.arrive("gatito.jpg", 1)

# b. imprima el primer documento de la cola (solamente mostrar el nombre de este por pantalla).
value = documents.attention()
print(
    f"""Imprime el primer documento y se elimina de la cola:
{value[1]}, {priorityParser(value[0])}(\033[31m{value[0]}\033[0m)
"""
)

# c. cargue dos documentos del staff de TI.
documents.arrive("informe.pdf", 2)
documents.arrive("procedimientos.docx", 2)

# d. cargue un documento del gerente.
documents.arrive("finanzas.pdf", 3)

# e. imprima los dos primeros documentos de la cola.
print("Imprime los 2 primeros documentos y se eliminan de la cola:")
for _ in range(2):
    value = documents.attention()
    print(f"{value[1]}, {priorityParser(value[0])}(\033[31m{value[0]}\033[0m)")
print()

# f. cargue dos documentos de empleados y uno de gerente.
documents.arrive("contrato.docx", 1)
documents.arrive("reporte_asistencia.xls", 1)
documents.arrive("plan_estrategico.pdf", 3)

# g. imprima todos los documentos de la cola de impresión.
print("Se imprime el resto de los documetnos de la cola:")
while documents.size() > 0:
    value = documents.attention()
    print(f"{value[1]}, {priorityParser(value[0])}(\033[31m{value[0]}\033[0m)")
