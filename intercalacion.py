# Ejercicio 1: Intercalacion
# Une los tickets de venta de dos sucursales ya ordenados en un solo archivo

def crear_archivos():
    norte = [
        "101,Refresco,22",
        "104,Galletas,18",
        "109,Cafe,35",
        "112,Agua,15",
        "118,Papas,25"
    ]
    sur = [
        "102,Jugo,20",
        "105,Pan,12",
        "109,Chocolate,28",
        "115,Yogurt,24",
        "120,Leche,30"
    ]
    with open("sucursal_norte.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(norte) + "\n")
    with open("sucursal_sur.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(sur) + "\n")


def ticket(linea):
    return int(linea.strip().split(",")[0])


def intercalar(arch1, arch2, salida):
    with open(arch1, "r", encoding="utf-8") as f1, \
         open(arch2, "r", encoding="utf-8") as f2, \
         open(salida, "w", encoding="utf-8") as out:

        l1 = f1.readline()
        l2 = f2.readline()

        while l1 and l2:
            if ticket(l1) <= ticket(l2):
                out.write(l1)
                l1 = f1.readline()
            else:
                out.write(l2)
                l2 = f2.readline()

        while l1:
            out.write(l1)
            l1 = f1.readline()

        while l2:
            out.write(l2)
            l2 = f2.readline()


if __name__ == "__main__":
    crear_archivos()
    intercalar("sucursal_norte.txt", "sucursal_sur.txt", "ventas_totales.txt")

    print("Ventas combinadas (ventas_totales.txt):")
    with open("ventas_totales.txt", "r", encoding="utf-8") as f:
        for linea in f:
            print(" ", linea.strip())