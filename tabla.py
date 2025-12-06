import numpy as np
from tabulate import tabulate



#   MOSTRAR TABLA
def mostrar_tabla(tabla):
    """Muestra la tabla con formato elegante usando 'tabulate'."""
    if not tabla:
        print("La tabla está vacía.")
        return

    print("\n=== TABLA ===")
    print(tabulate(tabla, headers="keys", tablefmt="fancy_grid"))


#   CARGAR TABLA

def cargar_tabla_estadistica():
    """
    Carga valores y frecuencias desde el usuario.
    Devuelve el nombre de la primera columna y la tabla
    Ademas valida que la frecuencia sea un numero con un try
    """
    nombre_columna = input("Ingrese el nombre de la primera columna: ")

    tabla = []

    print("\nIngrese los valores y frecuencias. Escriba 'end' para terminar.\n")

    while True:
        valor = input(f"{nombre_columna}: ")

        if valor.lower() == "end":
            break

        frecuencia = input("Frecuencia: ")

        if frecuencia.lower() == "end":
            break

        try:
            frecuencia = int(float(frecuencia))
        except ValueError:
            print("La frecuencia debe ser un número. Intente nuevamente.\n")
            continue

        fila = {
            nombre_columna: float(valor),
            "frecuencia": frecuencia
        }

        tabla.append(fila)
        print("Fila agregada.\n")

    return nombre_columna, tabla

#   ORDENAR TABLA

def ordenar_tabla(tabla, nombre_columna):
    """Ordena la tabla de menor a mayor según la columna ingresada."""
    try:
        return sorted(tabla, key=lambda x: float(x[nombre_columna]))
    except ValueError:
        return sorted(tabla, key=lambda x: x[nombre_columna])



#   AGREGAR ÍNDICES

def agregar_indices(tabla_ordenada):
    """Agrega un índice numérico a cada fila."""
    return [
        {"indice": i + 1, **fila}
        for i, fila in enumerate(tabla_ordenada)
    ]

#   EXPANDIR TABLA A LISTA

def tabla_a_lista(tabla):
    """
    Expande la tabla a una lista de valores según su frecuencia.
    Ejemplo: r=10 f=3 -> [10,10,10]
    """
    datos = []

    columnas = list(tabla[0].keys())
    columnas.remove("indice")
    columnas.remove("frecuencia")
    columna_valor = columnas[0]

    for fila in tabla:
        valor = float(fila[columna_valor])
        frecuencia = int(fila["frecuencia"])
        datos.extend([valor] * frecuencia)

    return np.array(datos)