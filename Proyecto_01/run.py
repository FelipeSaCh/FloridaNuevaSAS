#!/usr/bin/env python
"""
Script de ejecución principal para Proyecto_01.
Permite ejecutar el proyecto importando correctamente la carpeta 'src'.
"""
import os
import sys

# Asegurar que el directorio raíz de Proyecto_01 esté en el path de Python
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.main import main

if __name__ == "__main__":
    main()
