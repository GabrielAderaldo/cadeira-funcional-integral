import unittest
from src.integral_calculator import calcular_integral

class TestIntegralCalculator(unittest.TestCase):
    
    def test_calcular_integral(self):
        # Teste 1: Integral de x^2
        self.assertEqual(str(calcular_integral('x**2', 'x')), 'x**3/3')
        
        # Teste 2: Integral de sin(x)
        self.assertEqual(str(calcular_integral('sin(x)', 'x')), '-cos(x)')
        
        # Teste 3: Integral de e^x
        self.assertEqual(str(calcular_integral('exp(x)', 'x')), 'exp(x)')
        
        # Teste 4: Teste para polinômios de ordem superior
        self.assertEqual(str(calcular_integral('3*x**5 - 2*x**3 + x - 1', 'x')), 'x**6/2 - x**4/2 + x**2/2 - x')
        
        # Teste 5: Teste para funções trigonométricas:
        self.assertEqual(str(calcular_integral('sin(x)**2 + cos(x)**2', 'x')), 'x')

        # Teste 6: Teste para funções exponenciais mais complexas:
        self.assertEqual(str(calcular_integral('exp(2*x)', 'x')), 'exp(2*x)/2')

        # Teste 7: Teste para funções logarítmicas:
        self.assertEqual(str(calcular_integral('log(x)', 'x')), 'x*log(x) - x')
   
        # Teste 8: Teste para funções racionais:
        self.assertEqual(str(calcular_integral('1/(x**2)', 'x')), '-1/x')

        # Teste 9: Teste para funções trigonométricas inversas:
        self.assertEqual(str(calcular_integral('asin(x)', 'x')), 'x*asin(x) + sqrt(1 - x**2)')

if __name__ == '__main__':
    unittest.main()