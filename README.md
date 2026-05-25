# Florida Nueva SAS Scripts

Este repositorio contiene diversos scripts y archivos utilizados por Florida Nueva SAS.

## Estructura del Proyecto

*   **`Html_styles_js/`**: Contiene archivos HTML, plantillas y recursos relacionados con la interfaz y reportes (ej. plantillas de retención, perfil de cargo, seguridad social).
*   **`Python_scripts/`**: Contiene scripts en Python utilizados principalmente para el procesamiento de datos, comparación de libros, extracción de notas, conversión de archivos (Excel, CSV) y reestructuración de reportes tributarios.

## Requisitos
El proyecto utiliza un entorno virtual. Para ejecutar los scripts de Python, asegúrate de activar el entorno e instalar las dependencias necesarias.

## Actualizaciones Recientes

*   **Transformación de Estructura ICA (Mayo 2026)**: Se incorporó el script `transformacion_ica.py`, diseñado para normalizar y reestructurar reportes del Impuesto de Industria y Comercio (ICA). Este script toma un archivo Excel con columnas organizadas horizontalmente por bimestres/períodos y las convierte a un formato vertical normalizado (tipo base de datos). 
    *   **Columnas base procesadas**: NIT, Empresa, ReteICA, AutoRete, Municipio.
    *   **Períodos soportados**: Bimestres del 1 al 6 y Anticipo Parcial de Fin de Año.
    *   **Salida**: Archivo de Excel optimizado y limpio para auditoría y análisis de datos.
*   **Plantillas 2025**: Se ha actualizado la plantilla HTML (`00 PLANTILLA  RETENCION.html`) con los ajustes y formatos correspondientes al año 2025 (incluyendo la sección de firmas, totales y retenciones de impuestos). También se encuentra disponible la versión en PDF (`00 PLANTILLA  RETENCION  2025 USAR ESTA.pdf`) para referencia y uso.
*   **Formularios de Actas**: Se ha añadido un nuevo formulario HTML (`funciones.html`) diseñado para generar y presentar las actas de reuniones administrativas, incluyendo formatos estructurados para objetivos, asistentes y actividades realizadas.
