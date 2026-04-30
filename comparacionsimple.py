import pandas as pd

# ── Configuración de Rutas ─────────────────────────────────────────────────────
ARCHIVO_CLIENTES = r"D:\Escritorio\MANEJO GLIDE\recursos\clientes6.xlsx"
ARCHIVO_CAMARA   = r"C:\Users\Andres Sanchez\Downloads\SEGURIDAD SOCIAL (1).xls"
SALIDA           = r"D:\Escritorio\MANEJO GLIDE\Comparacionlibros\reporte_verificacion_nits_seguridadsocial.xlsx"

def ejecutar_proceso():
    print("1. Cargando base de datos de Clientes...")
    try:
        # Leemos solo la columna NIT de clientes para mayor velocidad
        df_cli = pd.read_excel(ARCHIVO_CLIENTES, dtype=str)
        # Buscamos la columna que contenga 'nit'
        col_nit_cli = next((c for c in df_cli.columns if 'nit' in str(c).lower()), None)
        
        if col_nit_cli:
            nits_validos = set(df_cli[col_nit_cli].str.strip())
        else:
            print("❌ No se encontró la columna NIT en el archivo de Clientes.")
            return
    except Exception as e:
        print(f"❌ Error al leer Clientes: {e}")
        return

    print("2. Procesando archivo de Cámara...")
    try:
        # Leer el nuevo formato de Cámara
        df_cam = pd.read_excel(ARCHIVO_CAMARA, dtype=str)
        
        # Validar que exista la columna NIT en origen
        if 'NIT' not in df_cam.columns:
            # Intento buscarla en minúsculas si no está exacta
            col_nit_cam = next((c for c in df_cam.columns if 'nit' in str(c).lower()), None)
            if col_nit_cam:
                df_cam.rename(columns={col_nit_cam: 'NIT'}, inplace=True)
            else:
                print("❌ No se encontró la columna NIT en el archivo de Cámara.")
                return

        print("3. Verificando NITS...")
        # Creamos la nueva columna comparando con el conjunto de nits_validos
        df_cam['ESTADO EN CLIENTES'] = df_cam['NIT'].str.strip().apply(
            lambda x: "ENCONTRADO" if x in nits_validos else "NO ENCONTRADO"
        )

        print("4. Guardando informe...")
        # Guardar manteniendo las columnas originales: RESPONSABLE, NIT, NOMBRE, USUARIO ISS, CLAVE ISS
        df_cam.to_excel(SALIDA, index=False)
        print(f"✅ Proceso terminado exitosamente. Archivo en: {SALIDA}")

    except Exception as e:
        print(f"❌ Ocurrió un error: {e}")

if __name__ == "__main__":
    ejecutar_proceso()