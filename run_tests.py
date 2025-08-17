import unittest
import sys

def main():
    # Cargar todos los tests del directorio 'test' que comiencen con 'test_'
    loader = unittest.TestLoader()
    start_dir = 'test'
    suite = loader.discover(start_dir, pattern='test_*.py')
    
    # Ejecutar los tests con salida detallada
    runner = unittest.TextTestRunner(verbosity=1)
    result = runner.run(suite)
    
    # Devolver 0 si todos pasaron, 1 si hubo fallos
    if result.wasSuccessful():
        return 0
    else:
        return 1

if __name__ == "__main__":
    sys.exit(main())
