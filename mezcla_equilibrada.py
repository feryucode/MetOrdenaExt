# Ejercicio 3: Mezcla Equilibrada
# Ordena un archivo de reportes de soporte con tramos parcialmente ordenados usando 4 archivos

def crear_reportes():
    reportes = [
        "301,Sin internet",
        "306,Impresora trabada",
        "314,Cambio de contrasena",
        "302,Pantalla azul",
        "309,Correo bloqueado",
        "320,Error en sistema",
        "304,Falla en teclado",
        "311,Actualizacion pendiente",
        "318,Red lenta",
        "305,Mouse no responde",
        "312,Audio desactivado"
    ]
    with open("reportes.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(reportes) + "\n")


def folio(linea):
    return int(linea.strip().split(",")[0])


def distribuir(origen, f1_nom, f2_nom):
    with open(origen, "r", encoding="utf-8") as f, \
         open(f1_nom, "w", encoding="utf-8") as f1, \
         open(f2_nom, "w", encoding="utf-8") as f2:

        linea = f.readline()
        if not linea:
            return

        actual = f1
        anterior = folio(linea)
        actual.write(linea)

        for linea in f:
            valor = folio(linea)
            if valor < anterior:
                actual = f2 if actual == f1 else f1
            actual.write(linea)
            anterior = valor


def fusionar_tramos(in1_nom, in2_nom, out1_nom, out2_nom):
    tramos = 0
    with open(in1_nom, "r", encoding="utf-8") as in1, \
         open(in2_nom, "r", encoding="utf-8") as in2, \
         open(out1_nom, "w", encoding="utf-8") as out1, \
         open(out2_nom, "w", encoding="utf-8") as out2:

        l1 = in1.readline()
        l2 = in2.readline()
        salida = out1

        while l1 or l2:
            fin1 = not bool(l1)
            fin2 = not bool(l2)

            while not fin1 and not fin2:
                v1, v2 = folio(l1), folio(l2)
                if v1 <= v2:
                    salida.write(l1)
                    l1 = in1.readline()
                    if not l1 or folio(l1) < v1:
                        fin1 = True
                else:
                    salida.write(l2)
                    l2 = in2.readline()
                    if not l2 or folio(l2) < v2:
                        fin2 = True

            while not fin1:
                v1 = folio(l1)
                salida.write(l1)
                l1 = in1.readline()
                if not l1 or folio(l1) < v1:
                    fin1 = True

            while not fin2:
                v2 = folio(l2)
                salida.write(l2)
                l2 = in2.readline()
                if not l2 or folio(l2) < v2:
                    fin2 = True

            tramos += 1
            salida = out2 if salida == out1 else out1

    return tramos


def esta_vacio(nombre):
    with open(nombre, "r", encoding="utf-8") as f:
        return f.readline() == ""


def mezcla_equilibrada(origen, salida_final):
    f1, f2, f3, f4 = "f1.txt", "f2.txt", "f3.txt", "f4.txt"
    distribuir(origen, f1, f2)

    entrada = (f1, f2)
    salida = (f3, f4)
    pasada = 1

    while not esta_vacio(entrada[1]):
        tramos = fusionar_tramos(entrada[0], entrada[1], salida[0], salida[1])
        print(f"Pasada {pasada}: quedaron {tramos} tramos")
        entrada, salida = salida, entrada
        pasada += 1

    with open(entrada[0], "r", encoding="utf-8") as src, \
         open(salida_final, "w", encoding="utf-8") as dst:
        dst.write(src.read())


if __name__ == "__main__":
    crear_reportes()
    mezcla_equilibrada("reportes.txt", "reportes_ordenados.txt")

    print("\nReportes ordenados:")
    with open("reportes_ordenados.txt", "r", encoding="utf-8") as f:
        for linea in f:
            print(" ", linea.strip())