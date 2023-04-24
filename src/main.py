from sympy import sympify, integrate, symbols

def calcular_integral(expressao, variavel, limite_inferior, limite_superior):
   
    expressao_sym = sympify(expressao)
    
   
    variavel_sym = symbols(variavel)
    
   
    integral_sym = integrate(expressao_sym, (variavel_sym, limite_inferior, limite_superior))
    
    
    return float(integral_sym)


resultado = calcular_integral("x**2", "x", 0, 1)
print(resultado)  