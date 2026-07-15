import unittest
import sys
import os

# Asegurar que el directorio raíz de Proyecto_01 esté en el path de Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils import saludo, sumar

class TestUtils(unittest.TestCase):
    def test_saludo_con_nombre(self):
        self.assertEqual(saludo("Carlos"), "¡Hola, Carlos!")

    def test_saludo_sin_nombre(self):
        self.assertEqual(saludo(""), "¡Hola, mundo!")

    def test_sumar(self):
        self.assertEqual(sumar(2, 3), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(0.5, 1.5), 2.0)
