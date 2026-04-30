import pandas as pd
import os
from tkinter import filedialog, Tk
from datetime import datetime

# Configuración de la ventana oculta de Tkinter
root = Tk()
root.withdraw()
root.attributes('-topmost', True)

# 1. Seleccionar el archivo (o archivos) mediante el explorador
print("Esperando selección de archivo...")
rutas_archivos = filedialog.askopenfilenames(
    title="Selecciona los archivos Excel para convertir",
    filetypes=[("Archivos de Excel", "*.xlsx *.xls")]
)

if not rutas_archivos:
    print("No se seleccionó ningún archivo. Saliendo...")
    exit()

# 2. Configuración de carpetas con fecha del día
fecha_hoy = datetime.now().strftime("%Y-%m-%d")  # Formato: 2026-04-23
ruta_base_salida = r"D:\Escritorio\MANEJO GLIDE\Conversionescsv\CSV_convertido"

# Crear la subcarpeta específica para el día de hoy
carpeta_del_dia = os.path.join(ruta_base_salida, fecha_hoy)

if not os.path.exists(carpeta_del_dia):
    print(f"Creando carpeta para el día de hoy: {fecha_hoy}")
    os.makedirs(carpeta_del_dia)

contador = 0

print(f"\nSe han seleccionado {len(rutas_archivos)} archivo(s).")
print(f"Los archivos se guardarán en: {carpeta_del_dia}")
print("="*50)

# 3. Procesar los archivos seleccionados
for ruta_xlsx in rutas_archivos:
    archivo_nombre = os.path.basename(ruta_xlsx)
    nombre_csv = os.path.splitext(archivo_nombre)[0] + ".csv"
    
    # La ruta de guardado ahora apunta a la carpeta del día
    ruta_csv = os.path.join(carpeta_del_dia, nombre_csv)

    try:
        print(f"Procesando: {archivo_nombre}")
        
        # Leer el Excel
        df = pd.read_excel(ruta_xlsx)
        
        # Guardar como CSV
        # utf-8-sig asegura que Excel abra bien los caracteres latinos
        df.to_csv(ruta_csv, index=False, encoding="utf-8-sig") 

        print(f"  ✓ Filas: {len(df)} | Columnas: {len(df.columns)}")
        print(f"  ✓ Convertido: {nombre_csv}\n")
        contador += 1

    except Exception as e:
        print(f"  ✗ Error al convertir {archivo_nombre}: {e}\n")

print("="*50)
print(f"Proceso finalizado.")
print(f"Total procesados hoy ({fecha_hoy}): {contador}")