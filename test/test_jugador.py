import unittest
from src.jugador import Participante

class TestParticipante(unittest.TestCase):
    def setUp(self):
        self.participante1 = Participante("Lucas", "X")
        self.participante2 = Participante("Ana", "O")
    
    def test_crear_participante(self):
        jugador = Participante("Prueba", "X")
        self.assertEqual(jugador.alias, "Prueba")
        self.assertEqual(jugador.simbolo, "X")
    
    def test_nombre(self):
        self.assertEqual(self.participante1.nombre(), "Lucas")
        self.assertEqual(self.participante2.nombre(), "Ana")
    
    def test_simbolo(self):
        self.assertEqual(self.participante1.ficha(), "X")
        self.assertEqual(self.participante2.ficha(), "O")
    
    def test_participantes_diferentes(self):
        otro = Participante("Pedro", "X")
        self.assertNotEqual(self.participante1.alias, otro.alias)
        self.assertEqual(self.participante1.simbolo, otro.simbolo)
    
    def test_participante_sin_simbolo(self):
        jugador = Participante("Desconocido", "")
        self.assertEqual(jugador.ficha(), "")
    
    def test_participante_sin_nombre(self):
        jugador = Participante("", "X")
        self.assertEqual(jugador.nombre(), "")


if __name__ == '__main__':
    unittest.main()
