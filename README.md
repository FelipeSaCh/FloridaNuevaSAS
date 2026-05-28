# Florida Nueva SAS Scripts

Este repositorio contiene diversos scripts y archivos utilizados por Florida Nueva SAS.

> [!NOTE]
> **Compatibilidad con Glide Apps**: Todos los archivos HTML en este repositorio se estructuran con sus estilos (`<style>`) y lógica de JavaScript (`<script>`) concatenados directamente en el mismo archivo. Esto responde a un requerimiento técnico estricto para permitir su correcta ejecución y renderizado dentro de la plataforma **Glide Apps**.

## Estructura del Proyecto

*   **`Html_styles_js/`**: Contiene archivos HTML y plantillas autónomas (ej. retenciones, perfiles de cargo, seguridad social, programaciones y resoluciones de facturación).
*   **`Python_scripts/`**: Contiene scripts en Python utilizados para el procesamiento de datos, comparación de libros, extracción de notas, conversión de formatos (Excel a CSV) y reestructuración de reportes.

## Requisitos
El proyecto utiliza un entorno virtual. Para ejecutar los scripts de Python, asegúrate de activar el entorno e instalar las dependencias necesarias.

## Actualizaciones Recientes

*   **Tarjetas de Resoluciones de Facturación (Mayo 2026)**: Se incorporó `Html_styles_js/cards_resoluciones.html`, una plantilla HTML premium autocontenida y diseñada en modo oscuro para el seguimiento visual de resoluciones de facturación. Permite visualizar estructuradamente datos del cliente, número de resolución, NIT, tipo de factura, prefijo, responsable y destaca visualmente en color rojo de alerta los días pendientes.
*   **Plantilla de Programación de Actividades (Mayo 2026)**: Se actualizó `Html_styles_js/index_programaciones.html`, una plantilla HTML diseñada en modo oscuro premium para mostrar tarjetas de actividades. Admite campos dinámicos para fecha de inicio/fin (`FECHAINICIO`, `FECHAFIN`), responsable (`NOMBRE`), descripción (`ACTIVIDAD`), cliente (`CLIENTE`) y estado/justificación (`TEXTRAZON`).
*   **Optimización del Conversor a CSV (Mayo 2026)**: Se actualizó `Python_scripts/convertiracsv_window.py` para hacer más portable el proceso de conversión de Excel a CSV. Ahora el script detecta automáticamente la carpeta de origen del archivo `.xlsx` seleccionado y guarda su correspondiente `.csv` en esa misma ubicación, eliminando rutas absolutas estáticas.
