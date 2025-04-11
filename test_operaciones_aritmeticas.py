import unittest
from operaciones_aritmeticas import OperacionesAritmeticas

class TestSuma(unittest.TestCase):
    def test_suma_dosNumeros_retornaSuma(self):
        # Arrange
        operando1 = 10
        operando2 = 15

        resultadoEsperado = 25

        objSuma = OperacionesAritmeticas(operando1, operando2)

        # Act
        resultadoActual = objSuma.calcularSuma()

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual, " Fallo la suma")

    def test_suma_operadorNoNumerico_lanzaExcepcion(self):
        objSuma = OperacionesAritmeticas(3, "a")
        with self.assertRaises(TypeError):
            objSuma.calcularSuma()

    def test_division_dosNumeros_retornaDivision(self):
        # Arrange
        dividendo = 10
        divisor = 15

        resultadoEsperado = 0.666

        objSuma = OperacionesAritmeticas(dividendo, divisor)

        # Act
        resultadoActual = objSuma.calcular_division()

        # Assert
        self.assertAlmostEqual(resultadoEsperado, resultadoActual, 2," Fallo la división")
    def test_division_operadorNoNumerico_lanzaExcepcion(self):
        objSuma = OperacionesAritmeticas(3, "a")
        with self.assertRaises(TypeError):
            objSuma.calcular_division()

    def test_division_divisorCero_lanzaExcepcion(self):
        objSuma = OperacionesAritmeticas(3, 0)
        with self.assertRaises(ZeroDivisionError):
            objSuma.calcular_division()
if __name__ == '__main__':
    unittest.main()
