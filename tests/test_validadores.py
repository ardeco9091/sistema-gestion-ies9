# -*- coding: utf-8 -*-
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from validadores import es_email_de_alumno_valido

class TestCalidadSoftware(unittest.TestCase):
    def test_camino_feliz(self):
        self.assertTrue(es_email_de_alumno_valido("alumno@ies9-juj.infd.edu.ar"))
    def test_rechazo_gmail(self):
        self.assertFalse(es_email_de_alumno_valido("test@gmail.com"))
if __name__ == '__main__':
    unittest.main()
