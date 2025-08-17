import unittest
from src.tresenraya import TresEnRaya

class TestTresEnRaya(unittest.TestCase):
    def setUp(self):
        self.juego = TresEnRaya()
    
    def test_crear_juego(self):
        self.assertIsNotNone(self.juego.participante1)
        self.assertIsNotNone(self.juego.participante2)
        self.assertIsNotNone(self.juego.en_turno)
        self.assertIsNotNone(self.juego.tablero)
        self.assertIsNone(self.juego.vencedor)
    
    def test_participantes_iniciales(self):
        self.assertEqual(self.juego.participante1.nombre(), "Jugador A")
        self.assertEqual(self.juego.participante1.ficha(), "X")
        self.assertEqual(self.juego.participante2.nombre(), "Jugador B")
        self.assertEqual(self.juego.participante2.ficha(), "O")
    
    def test_participante_inicial(self):
        self.assertEqual(self.juego.jugador_en_turno(), self.juego.participante1)
    
    def test_cambiar_turno(self):
        inicial = self.juego.jugador_en_turno()
        self.juego.marcar_casilla(0, 0)
        siguiente = self.juego.jugador_en_turno()
        
        self.assertNotEqual(inicial, siguiente)
    
    def test_victoria_fila(self):
        self.juego.marcar_casilla(0, 0)
        self.juego.marcar_casilla(1, 0)
        self.juego.marcar_casilla(0, 1)
        self.juego.marcar_casilla(1, 1)
        self.juego.marcar_casilla(0, 2)
        
        self.assertEqual(self.juego.quien_gano(), self.juego.participante1)
    
    def test_victoria_columna(self):
        self.juego.marcar_casilla(0, 0)
        self.juego.marcar_casilla(0, 1)
        self.juego.marcar_casilla(1, 0)
        self.juego.marcar_casilla(1, 1)
        self.juego.marcar_casilla(2, 0)
        
        self.assertEqual(self.juego.quien_gano(), self.juego.participante1)
    
    def test_victoria_diagonal_principal(self):
        self.juego.marcar_casilla(0, 0)
        self.juego.marcar_casilla(0, 1)
        self.juego.marcar_casilla(1, 1)
        self.juego.marcar_casilla(0, 2)
        self.juego.marcar_casilla(2, 2)
        
        self.assertEqual(self.juego.quien_gano(), self.juego.participante1)
    
    def test_victoria_diagonal_inversa(self):
        self.juego.marcar_casilla(0, 2)
        self.juego.marcar_casilla(0, 0)
        self.juego.marcar_casilla(1, 1)
        self.juego.marcar_casilla(1, 0)
        self.juego.marcar_casilla(2, 0)
        
        self.assertEqual(self.juego.quien_gano(), self.juego.participante1)
    
    def test_empate(self):
        movimientos = [
            (0, 0), (0, 1), (0, 2),
            (1, 1), (1, 0), (1, 2),
            (2, 1), (2, 0), (2, 2)
        ]
        
        for fila, columna i
