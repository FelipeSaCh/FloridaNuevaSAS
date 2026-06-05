# Florida Nueva SAS Scripts

Este repositorio contiene diversos scripts y archivos utilizados por Florida Nueva SAS.

> [!NOTE]
> **Compatibilidad con Glide Apps**: Todos los archivos HTML en este repositorio se estructuran con sus estilos (`<style>`) y lógica de JavaScript (`<script>`) concatenados directamente en el mismo archivo. Esto responde a un requerimiento técnico estricto para permitir su correcta ejecución y renderizado dentro de la plataforma **Glide Apps**.

## Estructura del Proyecto

*   **`Html_styles_js/`**: Contiene archivos HTML y plantillas autónomas (ej. retenciones, perfiles de cargo, seguridad social, programaciones, resoluciones de facturación, facturas, tareas asignadas, historiales de nómina y acuses de recibo).
*   **`Python_scripts/`**: Contiene scripts en Python utilizados para el procesamiento de datos, comparación de libros, extracción de notas, conversión de formatos (Excel a CSV), reestructuración de reportes y cruce/seguimiento de clientes.

## Requisitos
El proyecto utiliza un entorno virtual. Para ejecutar los scripts de Python, asegúrate de activar el entorno e instalar las dependencias necesarias.

## Actualizaciones Recientes

*   **Historial de Acuses Dinámico (Junio 2026)**: Se incorporó `Html_styles_js/acuse.html`, una plantilla HTML diseñada en modo oscuro premium con efecto *glassmorphism* para el seguimiento y visualización de ejecuciones de acuses de recibo. Al igual que el historial de nóminas, incluye un script automático de limpieza rápida adaptado para Glide Apps que descarta visualmente los meses sin registros.
*   **Mejoras Visuales y Animaciones CSS (Junio 2026)**: Se rediseñaron y optimizaron las transiciones de carga de `funciones.html`, `cards_resoluciones.html` y `nomina.html`. Se añadieron efectos de entrada suaves (`fadeIn`/`translateY`), sombras mejoradas y retrasos en cascada escalonados (*staggered delays*) para renderizar los elementos de forma secuencial. Adicionalmente, se anularon por completo las animaciones en el media print para garantizar la correcta exportación a PDF.
*   **Expansión de Seguimiento de Clientes (Junio 2026)**: Se añadió `Python_scripts/seguimiento_clientes.py`, un script en Python que realiza un cruce matricial (*cross join*) de un archivo de clientes con los 12 meses del año para estructurar un historial completo de seguimiento de forma masiva en `dataset_por_mes.csv`.
