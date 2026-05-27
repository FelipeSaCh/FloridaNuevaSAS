# Florida Nueva SAS Scripts

Este repositorio contiene diversos scripts y archivos utilizados por Florida Nueva SAS.

> [!NOTE]
> **Compatibilidad con Glide Apps**: Todos los archivos HTML en este repositorio se estructuran con sus estilos (`<style>`) y lógica de JavaScript (`<script>`) concatenados directamente en el mismo archivo. Esto responde a un requerimiento técnico estricto para permitir su correcta ejecución y renderizado dentro de la plataforma **Glide Apps**.

## Estructura del Proyecto

*   **`Html_styles_js/`**: Contiene archivos HTML y plantillas autónomas (ej. retenciones, perfiles de cargo, seguridad social y programaciones).
*   **`Python_scripts/`**: Contiene scripts en Python utilizados para el procesamiento de datos, comparación de libros, extracción de notas, conversión de formatos (Excel a CSV) y reestructuración de reportes.
*   **`workprophet_project/`**: Contiene cuadernos interactivos de Jupyter Notebook enfocados en analítica predictiva y estimación de la carga de trabajo diaria de la empresa mediante aprendizaje automático.

## Requisitos
El proyecto utiliza un entorno virtual. Para ejecutar los scripts de Python, asegúrate de activar el entorno e instalar las dependencias necesarias.

## Actualizaciones Recientes

*   **Modelo Predictivo de Carga de Trabajo - WorkProphet (Mayo 2026)**: Se incorporó la primera fase del proyecto con `workprophet_project/indexBeta.ipynb`. Este cuaderno de Jupyter entrena un modelo de regresión lineal para predecir dinámicamente el volumen de modificaciones y tareas diarias para los próximos 7 días, basándose en la fecha (día de la semana, día del mes) y métricas de ventana móvil de comportamiento histórico (`Lag Features` de 3 días).
*   **Plantilla de Programación de Actividades (Mayo 2026)**: Se actualizó `Html_styles_js/index_programaciones.html`, una plantilla HTML diseñada en modo oscuro premium para mostrar tarjetas de actividades. Admite campos dinámicos para fecha de inicio/fin (`FECHAINICIO`, `FECHAFIN`), responsable (`NOMBRE`), descripción (`ACTIVIDAD`), cliente (`CLIENTE`) y estado/justificación (`TEXTRAZON`).
*   **Optimización del Conversor a CSV (Mayo 2026)**: Se actualizó `Python_scripts/convertiracsv_window.py` para hacer más portable el proceso de conversión de Excel a CSV. Ahora el script detecta automáticamente la carpeta de origen del archivo `.xlsx` seleccionado y guarda su correspondiente `.csv` en esa misma ubicación, eliminando rutas absolutas estáticas.
*   **Transformación de Estructura ICA (Mayo 2026)**: Se incorporó el script `transformacion_ica.py`, diseñado para normalizar y reestructurar reportes del Impuesto de Industria y Comercio (ICA). Este script toma un archivo Excel con columnas horizontales por bimestres/períodos y las convierte a un formato vertical normalizado (tipo base de datos).
