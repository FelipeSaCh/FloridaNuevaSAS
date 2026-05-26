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

contador = 0
fecha_hoy = datetime.now().strftime("%Y-%m-%d")

print(f"\nSe han seleccionado {len(rutas_archivos)} archivo(s).")
print("="*50)

# 2. Procesar los archivos seleccionados
for ruta_xlsx in rutas_archivos:
    # Obtener la misma carpeta donde está guardado el archivo original
    carpeta_origen = os.path.dirname(ruta_xlsx)
    
    archivo_nombre = os.path.basename(ruta_xlsx)
    nombre_csv = os.path.splitext(archivo_nombre)[0] + ".csv"
    
    # La ruta de guardado ahora es la misma carpeta de origen
    ruta_csv = os.path.join(carpeta_origen, nombre_csv)

    try:
        print(f"Procesando: {archivo_nombre}")
        print(f"  -> Destino: {ruta_csv}")
        
        # Leer el Excel
        df = pd.read_excel(ruta_xlsx)
        
        # Guardar como CSV en la misma carpeta
        # utf-8-sig asegura que Excel abra bien los caracteres latinos
        df.to_csv(ruta_csv, index=False, encoding="utf-8-sig") 

        print(f"  ✓ Filas: {len(df)} | Columnas: {len(df.columns)}")
        print(f"  ✓ Convertido con éxito\n")
        contador += 1

    except Exception as e:
        print(f"  ✗ Error al convertir {archivo_nombre}: {e}\n")

print("="*50)
print(f"Proceso finalizado.")
print(f"Total procesados hoy ({fecha_hoy}): {contador}")