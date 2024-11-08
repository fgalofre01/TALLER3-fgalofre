import unittest
from Huron import Huron

class TestHurones(unittest.TestCase):
    def test_hacer_sonido(self):
        huron1 = Huron(nombre="huron1", peso=10.5, edad=6, pais_origen="Colombia", impuesto=0.16)
        self.assertIn(huron1.hacer_sonido(), "¡Eek Eek!")
        print(huron1.__dict__)
        

    def test_cacular_flete(self):
        huron1 = Huron(nombre="Roy", peso= 10.5, edad= 6, pais_origen="Colombia", impuesto=0.16)
        self.assertEqual(huron1.calcular_flete(), 1.68)
        print(huron1.__dict__)