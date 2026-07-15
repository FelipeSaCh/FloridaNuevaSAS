from io import BytesIO, StringIO
import pandas as pd
import streamlit as st

# 1. Configuración de la página (Debe ser la primera instrucción de Streamlit)
st.set_page_config(
    page_title="Lector de Archivos",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Lector de Archivos CSV y Excel")
st.write("Sube tu archivo para visualizar los datos de manera interactiva.")

# 2. Componente de subida de archivos
archivo_subido = st.file_uploader(
    "Selecciona o arrastra tu archivo (.csv o .xlsx)", type=["csv", "xlsx"]
)

if archivo_subido is not None:
    try:
        nombre_archivo = archivo_subido.name

        # 3. Leer el archivo según su extensión
        if nombre_archivo.endswith(".csv"):
            bytes_data = archivo_subido.read()
            try:
                texto = bytes_data.decode("utf-8")
            except UnicodeDecodeError:
                texto = bytes_data.decode("latin-1")

            # Detectar automáticamente si usa comas o punto y coma
            df = pd.read_csv(StringIO(texto), sep=None, engine="python")
        else:
            df = pd.read_excel(BytesIO(archivo_subido.read()))

        # Reemplazar valores nulos por celdas vacías
        df = df.fillna("")

        # 4. Mostrar métricas rápidas
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="Total de Filas", value=df.shape[0])
        with col2:
            st.metric(label="Total de Columnas", value=df.shape[1])

        # 5. Renderizar la tabla interactiva de Streamlit
        st.subheader("Vista Previa de los Datos")
        st.dataframe(df, use_container_width=True)

        st.success(f"¡Archivo '{nombre_archivo}' cargado con éxito!")

    except Exception as e:
        st.error(f"Ocurrió un error al procesar el archivo: {e}")
else:
    st.info("Por favor, sube un archivo para comenzar.")