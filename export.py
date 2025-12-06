from openpyxl import Workbook


def exportar_a_excel(nombre_archivo, nombre_columna, tabla, estadisticas):
    wb = Workbook()

    # Hoja 1: TABLA
    ws_tabla = wb.active
    ws_tabla.title = "Tabla"

    ws_tabla.append(["Índice", nombre_columna, "Frecuencia"])

    for fila in tabla:
        ws_tabla.append([
            fila["indice"],
            fila[nombre_columna],
            fila["frecuencia"]
        ])

    # Hoja 2: ESTADISTICAS
    ws_stats = wb.create_sheet("Estadisticas")
    ws_stats.append(["Medida", "Valor"])

    for clave, valor in estadisticas.items():
        ws_stats.append([clave, valor])

    wb.save(nombre_archivo)
    print(f"\nArchivo Excel generado exitosamente: {nombre_archivo}")