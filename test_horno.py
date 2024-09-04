import unittest
from Evidencia4 import Horno


import unittest


class TestHorno(unittest.TestCase):

    def setUp(self):
        self.horno = Horno(modelo="E0C3540X", marca="Electrolux", año_fabricación=2020)

    def test_encender_horno(self):
        self.horno.encender()
        self.assertEqual(self.horno.estado, "encendido")

    def test_apagar_horno(self):
        self.horno.encender()
        self.horno.apagar()
        self.assertEqual(self.horno.estado, "apagado")
        self.assertEqual(self.horno.temperatura_actual, 0)
        self.assertEqual(self.horno.temporizador, 0)
        self.assertIsNone(self.horno.modo_coccion)

    def test_controlar_temperatura(self):
        self.horno.encender()
        self.horno.controlar_temperatura(180)
        self.assertEqual(self.horno.temperatura_actual, 180)

    def test_controlar_temperatura_fuera_de_rango(self):
        self.horno.encender()
        with self.assertRaises(ValueError):
            self.horno.controlar_temperatura(300)

    def test_temperatura_sin_encender(self):
        with self.assertRaises(Exception):
            self.horno.controlar_temperatura(180)

    def test_establecer_temporizador(self):
        self.horno.encender()
        self.horno.establecer_temporizador(10)
        self.assertEqual(self.horno.temporizador, 10)

    def test_iniciar_temporizador(self):
        self.horno.encender()
        self.horno.establecer_temporizador(10)
        self.horno.iniciar_temporizador()

    def test_cambiar_modo_coccion(self):
        self.horno.encender()
        self.horno.cambiar_modo_coccion("Asar")
        self.assertEqual(self.horno.modo_coccion, "Asar")

    def test_cambiar_modo_coccion_sin_encender(self):
        with self.assertRaises(Exception):
            self.horno.cambiar_modo_coccion("Asar")

    def test_obtener_estado(self):
        self.horno.encender()
        self.horno.controlar_temperatura(180)
        self.horno.establecer_temporizador(10)
        self.horno.cambiar_modo_coccion("Asar")
        estado = self.horno.obtener_estado()
        self.assertEqual(estado["modelo"], "E0C3540X")
        self.assertEqual(estado["marca"], "Electrolux")
        self.assertEqual(estado["año_fabricación"], 2020)
        self.assertEqual(estado["estado"], "encendido")
        self.assertEqual(estado["temperatura_actual"], 180)
        self.assertEqual(estado["temporizador"], 10)
        self.assertEqual(estado["modo_coccion"], "Asar")

        print(estado)


if __name__ == "__main__":
    unittest.main()
