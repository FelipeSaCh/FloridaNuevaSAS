# Proyecto 01

Este es el proyecto base estructurado en Python. Proporciona una base sólida, limpia y extensible para comenzar a desarrollar tu aplicación.

## Estructura del Proyecto

La estructura de carpetas y archivos creada es la siguiente:

```text
Proyecto_01/
│
├── .gitignore              # Archivos y carpetas ignorados por Git
├── README.md               # Documentación general del proyecto (este archivo)
├── requirements.txt        # Dependencias de Python requeridas
├── run.py                  # Script de ejecución del punto de entrada principal
│
├── src/                    # Código fuente de la aplicación
│   ├── __init__.py         # Inicializador de paquete
│   ├── main.py             # Punto de entrada principal (lógica del programa)
│   └── utils.py            # Funciones auxiliares o utilidades
│
└── tests/                  # Pruebas unitarias
    ├── __init__.py         # Inicializador del paquete de pruebas
    └── test_main.py        # Casos de prueba para verificar el código
```

---

## Requisitos Previos

- Tener instalado **Python 3.8 o superior**.

---

## Configuración del Entorno de Desarrollo

Para mantener tus dependencias aisladas y no generar conflictos con otros proyectos, te recomendamos crear un entorno virtual:

1. **Crear el entorno virtual:**
   Abre una terminal en esta carpeta y ejecuta:
   ```bash
   python -m venv venv
   ```

2. **Activar el entorno virtual:**
   - **En Windows (PowerShell):**
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **En Windows (Símbolo del sistema / CMD):**
     ```cmd
     .\venv\Scripts\activate.bat
     ```
   - **En macOS / Linux:**
     ```bash
     source venv/bin/activate
     ```

3. **Instalar dependencias:**
   Una vez activado el entorno, instala los paquetes requeridos:
   ```bash
   pip install -r requirements.txt
   ```

---

## Cómo Ejecutar el Proyecto

Puedes iniciar el proyecto ejecutando el archivo `run.py` en la raíz de la carpeta `Proyecto_01`:

```bash
python run.py
```

Deberías ver una salida como la siguiente:
```text
--- Proyecto 01: Inicio de Aplicación ---
¡Hola, Usuario!
La suma de 5.0 y 7.5 es: 12.5
--- Proyecto 01: Ejecución Finalizada ---
```

---

## Cómo Ejecutar las Pruebas (Tests)

Puedes ejecutar las pruebas de dos maneras:

### Opción 1: Usando la biblioteca estándar (Sin instalar nada)
Este proyecto está preparado para ejecutarse directamente usando el módulo `unittest` integrado en Python:

```bash
python -m unittest discover -s tests
```

### Opción 2: Usando Pytest (Recomendado para desarrollo avanzado)
Si tienes instalado `pytest` (o después de instalar las dependencias con `requirements.txt`), simplemente ejecuta:

```bash
pytest
```
