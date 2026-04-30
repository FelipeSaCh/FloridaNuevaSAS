import pandas as pd
import os

# 1. Cargar el archivo de Excel
# Asegúrate de que el nombre del archivo sea el correcto
nombre_archivo = r"C:\Users\Andres Sanchez\Desktop\3333.xlsx"
excel_file = pd.ExcelFile(nombre_archivo)

# 2. Cargar las dos hojas en DataFrames
df_clientes = pd.read_excel(excel_file, sheet_name='Hoja1')
df_hoja1 = pd.read_excel(excel_file, sheet_name='Hoja2')

# 3. Identificar los registros de Hoja1 que NO están en clientes_ingresos
resultado = df_hoja1[~df_hoja1['NIT'].isin(df_clientes['NIT'])]

# 4. Definir nombre de salida
archivo_salida = 'Resultado_Diferencias2.xlsx'

# 5. Guardar el resultado
with pd.ExcelWriter(archivo_salida, engine='openpyxl') as writer:
    df_clientes.to_excel(writer, sheet_name='Hoja1', index=False)
    df_hoja1.to_excel(writer, sheet_name='Hoja2', index=False)
    resultado.to_excel(writer, sheet_name='Solo_en_Hoja1', index=False)

# 6. Imprimir resultados y ruta completa
ruta_completa = os.path.abspath(archivo_salida)
print("-" * 50)
print(f"Proceso terminado exitosamente.")
print(f"Registros nuevos encontrados: {len(resultado)}")
print(f"El archivo se guardó en:\n{ruta_completa}")
print("-" * 50)