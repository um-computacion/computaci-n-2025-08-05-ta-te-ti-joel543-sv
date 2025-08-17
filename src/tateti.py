from .tablero import TableroJuego
from .jugador import Participante

class TresEnRaya:
    def __init__(self):
        self.participante1 = Participante("Jugador A", "X")
        self.participante2 = Participante("Jugador B", "O")
        self.en_turno = self.participante1
        self.tablero = TableroJuego()
        self.vencedor = None
    
    def jugador_en_turno(self):
        return self.en_turno
    
    def hay_victoria(self, fila, columna):
        simbolo = self.tablero.matriz[fila][columna]
        
        # Revisión horizontal
        if all(self.tablero.matriz[fila][i] == simbolo for i in range(3)):
            return True
        
        # Revisión vertical
        if all(self.tablero.matriz[i][columna] == simbolo for i in range(3)):
            return True
        
        # Diagonal principal
        if fila == columna and all(self.tablero.matriz[i][i] == simbolo for i in range(3)):
            return True
        
        # Diagonal inversa
        if fila + columna == 2 and all(self.tablero.matriz[i][2 - i] == simbolo for i in range(3)):
            return True
        
        return False
    
    def hay_empate(self):
        return all(self.tablero.matriz[i][j] != "" for i in range(3) for j in range(3))
    
    def marcar_casilla(self, fila, columna):
        self.tablero.colocar_simbolo(fila, columna, self.en_turno.ficha())
        
        if self.hay_victoria(fila, columna):
            self.vencedor = self.en_turno
            return
        
        # Cambiar de turno
        if self.en_turno == self.participante1:
            self.en_turno = self.participante2
        else:
            self.en_turno = self.participante1
    
    def quien_gano(self):
        return self.vencedor
    
    def
