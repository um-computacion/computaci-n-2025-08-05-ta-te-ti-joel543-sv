class CasillaOcupadaError(Exception):
    pass


class TableroJuego:
    def __init__(self):
        self.matriz = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]

    def colocar_simbolo(self, fila, columna, simbolo):
        if self.matriz[fila][columna] == "":
            self.matriz[fila][columna] = simbolo
        else:
            raise CasillaOcupadaError("La casilla ya está ocupada")
