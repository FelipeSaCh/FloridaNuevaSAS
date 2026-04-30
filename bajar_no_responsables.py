import pandas as pd

def filtrar_periodicidad(archivo_origen, archivo_destino):
    try:
        # 1. Leer el archivo Excel original
        # Si tu archivo tiene varias hojas, puedes añadir sheet_name='NombreDeLaHoja'
        df = pd.read_excel(archivo_origen)

        # 2. Filtrar las filas donde la columna "PERIODICIDAD" sea exactamente "NO RESPONSABLE"
        # Usamos .strip() por si acaso hay espacios en blanco accidentales
        filtro = df[df['PERIOCIDAD'].astype(str).str.strip() == 'NO RESPONSABLE DE IVA']

        # 3. Verificar si se encontraron registros
        if not filtro.empty:
            # 4. Guardar el resultado en un nuevo archivo Excel
            # index=False evita que se agregue una columna de números al principio
            filtro.to_excel(archivo_destino, index=False)
            print(f"¡Éxito! Se han guardado {len(filtro)} filas en '{archivo_destino}'.")
        else:
            print("No se encontraron filas con el valor 'NO RESPONSABLE'.")

    except FileNotFoundError:
        print("Error: No se encontró el archivo de origen.")
    except KeyError:
        print("Error: No se encontró la columna 'PERIODICIDAD'. Revisa que el nombre esté escrito igual (mayúsculas/acentos).")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --- Configuración ---
archivo_entrada =r"C:\Users\Andres Sanchez\Desktop\Libro2.xlsx"
archivo_salida =r"D:\Escritorio\MANEJO GLIDE\recursos\resultado_filtrado.xlsx"

filtrar_periodicidad(archivo_entrada, archivo_salida)