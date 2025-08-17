from .tresenraya import TresEnRaya

def iniciar():
    print("¡Bienvenidos al Tres en Raya!")
    while True:
        partida = TresEnRaya()
        
        while not partida.esta_finalizada():
            print("Estado del tablero: ")
            print(partida.tablero.matriz)
            jugador_turno = partida.jugador_en_turno()
            print(f"Le toca a: {jugador_turno.nombre()} ({jugador_turno.simbolo()})")
            
            try:
                fila = int(input("Elegí la fila: "))
                columna = int(input("Elegí la columna: "))
                partida.marcar_casilla(fila, columna)
            except Exception as error:
                print(error)
        
        print("Tablero definitivo: ")
        print(partida.tablero.matriz)
        
        ganador = partida.quien_gano()
        if ganador:
            print(f"¡{ganador.nombre()} es el vencedor!")
        else:
            print("La partida terminó en empate.")
        
        otra = input("¿Querés jugar de nuevo? (s/n): ").lower()
        if otra != 's':
            break
    
    print("Juego finalizado.")

if __name__ == '__main__':
    iniciar()
