import os
import pandas as pd

# Ruta de la carpeta donde están los XLSX
carpeta_origen = r"D:\Escritorio\MANEJO GLIDE\recursos\resultado_filtrado.xlsx"

carpeta_salida = r"D:\Escritorio\MANEJO GLIDE\Conversionescsv\CSV_convertido"

# Verificar si la carpeta de origen existe
if not os.path.exists(carpeta_origen):
    print(f"ERROR: La carpeta de origen no existe: {carpeta_origen}")
    print("Verifica que la ruta sea correcta y que la carpeta esté creada.")
    exit()

# Crear la carpeta de salida si no existe
if not os.path.exists(carpeta_salida):
    print(f"La carpeta de salida no existe. Creándola: {carpeta_salida}")
    os.makedirs(carpeta_salida)

contador = 0

# Mostrar archivos encontrados para depuración
print("Archivos encontrados en la carpeta de origen:")
for archivo in os.listdir(carpeta_origen):
    print(f"  - {archivo}")

print("\n" + "="*50 + "\n")

# Recorrer todos los archivos dentro de la carpeta
for archivo in os.listdir(carpeta_origen):
    if archivo.lower().endswith(".xlsx"):
        ruta_xlsx = os.path.join(carpeta_origen, archivo)
        contador += 1

        # Nombre nuevo del archivo .csv
        nombre_csv = archivo[:-5] + ".csv"
        ruta_csv = os.path.join(carpeta_salida, nombre_csv)

        try:
            print(f"Procesando: {archivo}")
            
            # Leer el Excel
            df = pd.read_excel(ruta_xlsx)
            
            # Mostrar información del archivo leído
            print(f"  - Filas: {len(df)}, Columnas: {len(df.columns)}")

            # Guardar como CSV
            df.to_csv(ruta_csv, index=False, encoding="utf-8")

            print(f"  ✓ Convertido: {archivo} → {nombre_csv}\n")

        except Exception as e:
            contador -= 1
            print(f"  ✗ Error al convertir {archivo}: {e}\n")

print(f"Total de archivos procesados exitosamente: {contador}")