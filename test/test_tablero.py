import unittest
from src.tablero import TableroJuego, CasillaOcupadaError

class TestTableroJuego(unittest.TestCase):
    def setUp(self):
        self.tablero = TableroJuego()
    
    def test_crear_tablero(self):
        self.assertEqual(len(self.tablero.matriz), 3)
        self.assertEqual(len(self.tablero.matriz[0]), 3)
        self.assertEqual(len(self.tablero.matriz[1]), 3)
        self.assertEqual(len(self.tablero.matriz[2]), 3)
        
        for fila in self.tablero.matriz:
            for casilla in fila:
                self.assertEqual(casilla, "")
    
    def test_colocar_simbolo_valido(self):
        self.tablero.colocar_simbolo(0, 0, "X")
        self.assertEqual(self.tablero.matriz[0][0], "X")
        
        self.tablero.colocar_simbolo(1, 1, "O")
        self.assertEqual(self.tablero.matriz[1][1], "O")
        
        self.tablero.colocar_simbolo(2, 2, "X")
        self.assertEqual(self.tablero.matriz[2][2], "X")
    
    def test_colocar_simbolo_en_casilla_ocupada(self):
        self.tablero.colocar_simbolo(0, 0, "X")
        
        with self.assertRaises(CasillaOcupadaError):
            self.tablero.colocar_simbolo(0, 0, "O")
    
    def test_colocar_simbolos_diferentes(self):
        self.tablero.colocar_simbolo(0, 0, "X")
        self.tablero.colocar_simbolo(0, 1, "O")
        self.tablero.colocar_simbolo(1, 0, "X")
        
        self.assertEqual(self.tablero.matriz[0][0], "X")
        self.assertEqual(self.tablero.matriz[0][1], "O")
        self.assertEqual(self.tablero.matriz[1][0], "X")
    
    def test_colocar_simbolos_en_esquinas(self):
        self.tablero.colocar_simbolo(0, 0, "X")
        self.tablero.colocar_simbolo(0, 2, "O")
        self.tablero.colocar_simbolo(2, 0, "X")
        self.tablero.colocar_simbolo(2, 2, "O")
        
        self.assertEqual(self.tablero.matriz[0][0], "X")
        self.assertEqual(self.tablero.matriz[0][2], "O")
        self.assertEqual(self.tablero.matriz[2][0], "X")
        self.assertEqual(self.tablero.matriz[2][2], "O")
    
    def test_colocar_simbolo_en_centro(self):
        self.tablero.colocar_simbolo(1, 1, "X")
        self.assertEqual(self.tablero.matriz[1][1], "X")
    
    def test_colocar_simbolo_vacio(self):
        self.tablero.colocar_simbolo(0, 0, "")
        self.assertEqual(self.tablero.matriz[0][0], "")
    
    def test_colocar_simbolo_especial(self):
        self.tablero.colocar_simbolo(0, 0, "★")
        self.tablero.colocar_simbolo(1, 1, "♦")
        
        self.assertEqual(self.tablero.matriz[0][0], "★")
        self.assertEqual(self.tablero.matriz[1][1], "♦")


if __name__ == '__main__':
    unittest.main()
