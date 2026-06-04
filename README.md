# Florida Nueva SAS Scripts

Este repositorio contiene diversos scripts y archivos utilizados por Florida Nueva SAS.

> [!NOTE]
> **Compatibilidad con Glide Apps**: Todos los archivos HTML en este repositorio se estructuran con sus estilos (`<style>`) y lógica de JavaScript (`<script>`) concatenados directamente en el mismo archivo. Esto responde a un requerimiento técnico estricto para permitir su correcta ejecución y renderizado dentro de la plataforma **Glide Apps**.

## Estructura del Proyecto

*   **`Html_styles_js/`**: Contiene archivos HTML y plantillas autónomas (ej. retenciones, perfiles de cargo, seguridad social, programaciones, resoluciones de facturación, facturas, tareas asignadas e historiales de nómina).
*   **`Python_scripts/`**: Contiene scripts en Python utilizados para el procesamiento de datos, comparación de libros, extracción de notas, conversión de formatos (Excel a CSV), reestructuración de reportes y cruce/seguimiento de clientes.

## Requisitos
El proyecto utiliza un entorno virtual. Para ejecutar los scripts de Python, asegúrate de activar el entorno e instalar las dependencias necesarias.

## Actualizaciones Recientes

*   **Historial de Nóminas Dinámico (Junio 2026)**: Se incorporó `Html_styles_js/nomina.html`, una plantilla HTML diseñada con efectos de difuminado de fondo (*glassmorphism*) para el control y visualización de ejecuciones de nómina. Incluye un script en JavaScript de auto-limpieza periódica adaptado para Glide Apps, el cual remueve de forma automática y transparente del listado visual las filas/meses que no posean datos reales inyectados.
*   **Expansión de Seguimiento de Clientes (Junio 2026)**: Se añadió `Python_scripts/seguimiento_clientes.py`, un script en Python que realiza un cruce matricial (*cross join*) de un archivo de clientes con los 12 meses del año para estructurar un historial completo de seguimiento de forma masiva en `dataset_por_mes.csv`.
*   **Plantilla de Facturación Simple (Junio 2026)**: Se añadió `Html_styles_js/facturacion.html`, una plantilla HTML minimalista para la visualización de comprobantes de facturación (descripción, cantidad, precio e impuestos).
*   **Parametrización de la Tarjeta de Tareas (Junio 2026)**: Se actualizó `Html_styles_js/Tareas.html` reemplazando los valores de prueba estáticos por marcadores dinámicos estándar (como `TEXTCLIENTE`, `TEXTDIRIGIDO`, `TEXTEMAIL`, `TEXTTAREA`, `TEXTFECHA`, `TEXTOBSERVACIÓN`, `TEXTCREADO`) para su integración directa con Glide Apps.
