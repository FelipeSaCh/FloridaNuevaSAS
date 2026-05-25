import pandas as pd

def transformar_estructura_excel(ruta_archivo_original, ruta_archivo_salida):
    # 1. Cargar el archivo original de Excel
    # (Ajustar 'sheet_name' si tu tabla no está en la primera pestaña)
    df = pd.read_excel(ruta_archivo_original)
    
    # 2. Definir los bloques de bimestres/periodos basándonos en el orden exacto de tus columnas:
    # Columnas Base (0 a 4): 0:NIT, 1:EMPRESA, 2:RETEICA, 3:AUTORETE, 4:MUNICIPIO
    # Luego cada periodo tiene 3 columnas seguidas (Fecha/Bimestre, Presentado, Pagado)
    bloques_periodos = [
        {"etiqueta": "1", "idx_fecha": 5, "idx_pres": 6, "idx_pag": 7},
        {"etiqueta": "2", "idx_fecha": 8, "idx_pres": 9, "idx_pag": 10},
        {"etiqueta": "3", "idx_fecha": 11, "idx_pres": 12, "idx_pag": 13},
        {"etiqueta": "4", "idx_fecha": 14, "idx_pres": 15, "idx_pag": 16},
        {"etiqueta": "5", "idx_fecha": 17, "idx_pres": 18, "idx_pag": 19},
        {"etiqueta": "ANTICIPO PARCIAL FIN DE AÑO", "idx_fecha": 20, "idx_pres": 21, "idx_pag": 22},
        {"etiqueta": "6", "idx_fecha": 23, "idx_pres": 24, "idx_pag": 25},
    ]
    
    filas_transformadas = []
    
    # 3. Iterar fila por fila sobre el archivo original para normalizar los datos
    for _, fila in df.iterrows():
        # Extraer los datos fijos del tercero/municipio
        nit = fila.iloc[0]
        empresa = fila.iloc[1]
        reteica = fila.iloc[2]
        autorete = fila.iloc[3]
        municipio = fila.iloc[4]
        
        # Desempaquetar las columnas horizontales en filas verticales
        for bloque in bloques_periodos:
            fecha_bimestre = fila.iloc[bloque["idx_fecha"]]
            presentado = fila.iloc[bloque["idx_pres"]]
            pagado = fila.iloc[bloque["idx_pag"]]
            
            # Filtro para evitar agregar filas completamente vacías en bimestres que no se usan,
            # pero asegurando que se mantengan los registros válidos o estructuras como el Anticipo.
            if pd.notna(fecha_bimestre) and str(fecha_bimestre).strip() != "":
                filas_transformadas.append({
                    'NIT': nit,
                    'EMPRESA': empresa,
                    'RETEICA': reteica,
                    'AUTORETE': autorete,
                    'MUNICIPIO': municipio,
                    'BIMESTRE': bloque["etiqueta"],
                    'FECHA BIMESTRE': fecha_bimestre,
                    'PRESENTADO': presentado,
                    'PAGADO': pagado
                })
            elif bloque["etiqueta"] == "ANTICIPO PARCIAL FIN DE AÑO" and (pd.notna(presentado) or pd.notna(pagado)):
                filas_transformadas.append({
                    'NIT': nit,
                    'EMPRESA': empresa,
                    'RETEICA': reteica,
                    'AUTORETE': autorete,
                    'MUNICIPIO': municipio,
                    'BIMESTRE': bloque["etiqueta"],
                    'FECHA BIMESTRE': fecha_bimestre if pd.notna(fecha_bimestre) else "",
                    'PRESENTADO': presentado,
                    'PAGADO': pagado
                })
                
    # 4. Crear el nuevo DataFrame reestructurado
    df_reestructurado = pd.DataFrame(filas_transformadas)
    
    # 5. Exportar al nuevo archivo Excel normalizado
    df_reestructurado.to_excel(ruta_archivo_salida, index=False)
    print(f"¡Proceso completado con éxito! Archivo guardado en: {ruta_archivo_salida}")

# --- Ejemplo de Uso ---
transformar_estructura_excel(r"C:\Users\USUARIO\Desktop\Libro3.xlsx", r"C:\Users\USUARIO\Desktop\Resultado_Estructura_Reducida.xlsx")