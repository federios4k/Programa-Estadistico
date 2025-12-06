from tabla import (
    cargar_tabla_estadistica,
    ordenar_tabla,
    agregar_indices,
    mostrar_tabla,
    tabla_a_lista
)

from stats import (
    calcular_estadisticas,
    calcular_media,
    varianza_poblacional,
    intervalo_media,
    intervalo_varianza
)

from export import (
    exportar_a_excel
)

def menu_principal(tabla_final):
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Calcular media poblacional")
        print("2. Calcular varianza poblacional")
        print("3. Calcular intervalo de confianza de la MEDIA")
        print("4. Calcular intervalo de confianza de la VARIANZA")
        print("5. Ingresar una nueva tabla")
        print("6. Salir")
        print("====================================")

        opcion = input("Seleccioná una opción: ")

        # =============================
        # 1. MEDIA POBLACIONAL
        # =============================
        if opcion == "1":
            datos = tabla_a_lista(tabla_final)
            resultado = calcular_media(datos)
            print(f"\nMedia poblacional estimada: {resultado}")

        # =============================
        # 2. VARIANZA POBLACIONAL
        # =============================
        elif opcion == "2":
            datos = tabla_a_lista(tabla_final)
            resultado = varianza_poblacional(datos)
            print(f"\nVarianza poblacional estimada: {resultado}")

        # =============================
        # 3. INTERVALO MEDIA
        # =============================
        elif opcion == "3":
            datos = tabla_a_lista(tabla_final)
            c = float(input("Nivel de confianza (0.90, 0.95, 0.99): ").replace(",", "."))
            li, ls = intervalo_media(datos, c)
            print(f"\nIC para la media ({c*100}%): ({li}, {ls})")

        # =============================
        # 4. INTERVALO VARIANZA
        # =============================
        elif opcion == "4":
            datos = tabla_a_lista(tabla_final)
            c = float(input("Nivel de confianza (0.90, 0.95, 0.99): ").replace(",", "."))
            li, ls = intervalo_varianza(datos, c)
            print(f"\nIC para la varianza ({c*100}%): ({li}, {ls})")

        # =============================
        # 5. NUEVA TABLA
        # =============================
        elif opcion == "5":
            print("\nCargando nueva tabla...")
            ejecutar_flujo_principal()
            return

        # =============================
        # 6. SALIR
        # =============================
        elif opcion == "6":
            print("\nSaliendo del programa...")
            exit()

        else:
            print("Opción inválida. Intente nuevamente.")


def ejecutar_flujo_principal():
    # 1. Cargar la tabla
    nombre_columna, tabla = cargar_tabla_estadistica()

    # 2. Ordenar tabla
    tabla_ordenada = ordenar_tabla(tabla, nombre_columna)

    # 3. Agregar índices
    tabla_final = agregar_indices(tabla_ordenada)

    # 4. Mostrar tabla
    mostrar_tabla(tabla_final)

    # 5. Preparar datos para estadísticas
    datos = tabla_a_lista(tabla_final)
    estadisticas = calcular_estadisticas(datos)

    # 6. Exportar a Excel
    nombre_archivo = "resultado.xlsx"
    exportar_a_excel(nombre_archivo, nombre_columna, tabla_final, estadisticas)

    # 7. Ir al menú principal
    menu_principal(tabla_final)

if __name__ == "__main__":
    ejecutar_flujo_principal()
