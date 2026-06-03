import pandas as pd

# 1. Cargar tu archivo CSV original
# Cambia 'tus_clientes.csv' por el nombre real de tu archivo
df_original = pd.read_csv(r"C:\Users\USUARIO\Downloads\seguimiento de clientes (1).csv")

# 2. Crear un DataFrame temporal que solo contenga los 12 meses
meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre",
]
df_meses = pd.DataFrame({"Mes": meses})

# 3. Si tienes una versión de pandas reciente (1.2.0 o superior):
# Podemos usar el método 'how="cross"' para multiplicar cada fila por cada mes.
df_resultado = df_original.merge(df_meses, how="cross")

# --- ALTERNATIVA EN CASO DE ERROR ---
# Si tu versión de pandas es antigua y te da error el paso anterior,
# borra el '#' de las siguientes 3 líneas y comenta la línea del 'how="cross"':
# df_original['_key'] = 1
# df_meses['_key'] = 1
# df_resultado = df_original.merge(df_meses, on='key').drop('_key', axis=1)
# -------------------------------------

# 4. Reordenar las columnas para que 'Mes' quede junto a 'CLIENTES' (Opcional, por estética)
# Traemos 'Mes' al principio o después de CLIENTES si así lo deseas
columnas = list(df_resultado.columns)
columnas.remove("Mes")
# Insertar 'Mes' justo después de la columna 'CLIENTES'
posicion_clientes = columnas.index("CLIENTE")
columnas.insert(posicion_clientes + 1, "Mes")
df_resultado = df_resultado[columnas]

# 5. Guardar todo el dataset expandido en un nuevo archivo CSV
df_resultado.to_csv("dataset_por_mes.csv", index=False, encoding="utf-8-sig")

print(
    "¡Proceso completado! El dataset completo con la columna 'Mes' se guardó como 'dataset_por_mes.csv'."
)
print(df_resultado.head(14))  # Muestra las primeras filas para verificar