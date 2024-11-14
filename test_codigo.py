import unittest
from codigo import multiplicar

class TestMultiplicar(unittest.TestCase):
    def test_multiplicar(self):
        self.assertEqual(multiplicar(2, 3), 6)  # Prueba que 2x3=6
        self.assertEqual(multiplicar(0, 5), 0)  # Prueba que 0x5=0
        self.assertEqual(multiplicar(-1, 5), -5)  # Prueba que -1x5=-5

if __name__ == '__main__':
    unittest.main()
