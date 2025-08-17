**Alumno:** Joel Reynoso  Legajo:62300
## Estructura del Proyecto
```
├── src/
│   ├── __init__.py
│   ├── participante.py    # Clase Participante
│   ├── tablero_juego.py   # Clase TableroJuego
│   ├── tresenraya.py      # Clase TresEnRaya (lógica del juego)
│   └── consola.py         # Interfaz de línea de comandos
├── test/
│   ├── __init__.py
│   ├── test_participante.py
│   ├── test_tablero_juego.py
│   └── test_tresenraya.py
├── main.py                # Punto de entrada del juego
├── run_tests.py           # Ejecutor de pruebas
└── README.md
```
## Clases Implementadas
## Participante

Maneja el nombre y símbolo de cada jugador

Métodos: obtener_nombre(), obtener_simbolo()

## TableroJuego

Gestiona el tablero 3x3

Métodos: colocar_simbolo(fila, columna, simbolo)

Excepción: CeldaOcupadaError para posiciones ocupadas

## TresEnRaya

Controla la lógica del juego

Maneja turnos y verifica victoria/empate

Métodos: marcar_casilla(), hay_ganador(), hay_empate()

## Consola

Interfaz de usuario por línea de comandos

Maneja entrada de datos y muestra el estado del juego

## Ejecutar el Juego
python main.py

## Ejecutar las Pruebas
python run_tests.py

## Instrucciones del Juego

Para colocar una ficha, ingresa:

Fila (0, 1 o 2)

Columna (0, 1 o 2)

