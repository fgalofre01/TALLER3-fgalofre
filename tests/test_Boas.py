import unittest
from Boa_Constrictor import Boa_Constrictor
from Guarderia import Guarderia

class TestBoas(unittest.TestCase):
    def test_hacer_sonido(self):
        boa1 = Boa_Constrictor(nombre="Boa1", peso=25.5, edad=10, pais_origen="Colombia", impuesto=0.16)
        self.assertIn(boa1.hacer_sonido(), "¡Tsss!")
        print(boa1.__dict__)

    def test_cacular_flete(self):
        boa1 = Boa_Constrictor(nombre="Boa1", peso=25.5, edad=10, pais_origen="Colombia", impuesto=0.16)
        self.assertEqual(boa1.calcular_flete(), 4.08)
        print(boa1.__dict__)
    
    def test_alimentar_boas(self):
        # Se inicializa la guardería y una de sus boas
        guarderia = Guarderia()
        boa1 = guarderia.boas[0]
        # Se alimenta la boa hasta 5 ratones y verificamos el contador
        for _ in range(10):
          self.assertEqual(boa1.comer_raton(), boa1._ratones_comidos)
         # Alimentamos la boa usando el método alimentar_boa
        self.assertEqual(guarderia.alimentar_boa(boa1),"Exito")# Sexta alimentación
         # Alimentar hasta el límite
        for _ in range(9):
            guarderia.alimentar_boa(boa1)
        # Intentar alimentar más allá del límite
        self.assertEqual(guarderia.alimentar_boa(boa1), "La boa esta llena, Demasiado ratones!")
        # Intentar alimentar una boa inexistente
        self.assertEqual(guarderia.alimentar_boa(None), "Esta Boa no existe!")
        print(boa1.__dict__)
    