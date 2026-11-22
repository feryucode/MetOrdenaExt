# Ejercicio 2: Mezcla Directa
# Ordena un archivo de productos desordenados por codigo usando dos archivos auxiliares

def crear_inventario():
    productos = [
        "405,Teclado,450",
        "112,Mouse,180",
        "890,Monitor,2800",
        "103,Cable USB,95",
        "620,Audifonos,520",
        "215,Memoria 64GB,160",
        "530,Webcam,690",
        "108,Adaptador HDMI,140",
        "740,Bocinas,390"
    ]
    with open("inventario.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(productos) + "\n")


def codigo(linea):
    return int(linea.strip().split(",")[0])


def particionar(origen, aux1, aux2, tam_bloque):
    with open(origen, "r", encoding="utf-8") as f, \
         open(aux1, "w", encoding="utf-8") as f1, \
         open(aux2, "w", encoding="utf-8") as f2:

        linea = f.readline()
        while linea:
            for _ in range(tam_bloque):
                if not linea:
                    break
                f1.write(linea)
                linea = f.readline()

            for _ in range(tam_bloque):
                if not linea:
                    break
                f2.write(linea)
                linea = f.readline()


def fusionar(aux1, aux2, destino, tam_bloque):
    with open(aux1, "r", encoding="utf-8") as f1, \
         open(aux2, "r", encoding="utf-8") as f2, \
         open(destino, "w", encoding="utf-8") as out:

        l1 = f1.readline()
        l2 = f2.readline()

        while l1 or l2:
            c1 = 0
            c2 = 0

            while c1 < tam_bloque and c2 < tam_bloque and l1 and l2:
                if codigo(l1) <= codigo(l2):
                    out.write(l1)
                    l1 = f1.readline()
                    c1 += 1
                else:
                    out.write(l2)
                    l2 = f2.readline()
                    c2 += 1

            while c1 < tam_bloque and l1:
                out.write(l1)
                l1 = f1.readline()
                c1 += 1

            while c2 < tam_bloque and l2:
                out.write(l2)
                l2 = f2.readline()
                c2 += 1


def mezcla_directa(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        total = sum(1 for _ in f)

    tam_bloque = 1
    pasada = 1
    while tam_bloque < total:
        particionar(archivo, "aux1.txt", "aux2.txt", tam_bloque)
        fusionar("aux1.txt", "aux2.txt", archivo, tam_bloque)
        print(f"Pasada {pasada} lista (bloques de {tam_bloque})")
        tam_bloque *= 2
        pasada += 1


if __name__ == "__main__":
    crear_inventario()
    mezcla_directa("inventario.txt")

    print("\nInventario ordenado:")
    with open("inventario.txt", "r", encoding="utf-8") as f:
        for linea in f:
            print(" ", linea.strip())