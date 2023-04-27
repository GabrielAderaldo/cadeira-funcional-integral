from sympy import sympify, integrate, symbols, Eq, solve
from sympy.integrals import manualintegrate
from sympy.integrals.manualintegrate import integral_steps

def detect_integration_method(expression, variable):
    result = manualintegrate.manualintegrate(expression, variable)
    return result.__class__.__name__

def calcular_integral(expressao, variavel, metodo, limite_inferior=None, limite_superior=None):
    expressao_sym = sympify(expressao)
    variavel_sym = symbols(variavel)
    
    # Integração por substituição
    if metodo == "Integração por substituição":
        u = symbols('u')
        equation = Eq(u, expressao_sym.subs(variavel_sym, u))
        solved_expr = solve(equation, variavel_sym)[0]
        du = solved_expr.diff(u)
        new_expression = expressao_sym.subs(variavel_sym, solved_expr) * du
        integral_sym = integrate(new_expression, (u, limite_inferior, limite_superior)).subs(u, solved_expr)

    # Integração por partes
    elif metodo == "Integração por partes":
        steps = integral_steps(expressao_sym, variavel_sym)
        u = steps.u
        dv = steps.dv
        du = u.diff(variavel_sym)
        v = integrate(dv, variavel_sym)
        integral_sym = u * v - integrate(v * du, (variavel_sym, limite_inferior, limite_superior))

    # Integração por frações parciais
    elif metodo == "Integração por frações parciais":
        from sympy import apart
        partial_fractions_expression = apart(expressao_sym, variavel_sym)
        integral_sym = integrate(partial_fractions_expression, (variavel_sym, limite_inferior, limite_superior))

    # Método automático
    else:
        integral_sym = integrate(expressao_sym, (variavel_sym, limite_inferior, limite_superior))

    try:
        return float(integral_sym)
    except TypeError:
        return integral_sym

def main():
    print("Bem-vindo à Calculadora de Integrais!")
    
    expressao = input("Digite a expressão a ser integrada: ")
    variavel = input("Digite a variável de integração: ")
    limite_inferior = sympify(input("Digite o limite inferior de integração: "))
    limite_superior = sympify(input("Digite o limite superior de integração: "))
    
    print("\nMétodos de integração disponíveis:")
    print("1. Automático (detectar o melhor método/outros métodos não listados)")
    print("2. Integração por substituição")
    print("3. Integração por partes")
    print("4. Integração por frações parciais")
    
    metodo_selecionado = int(input("\nEscolha o método de integração (digite o número correspondente): "))
    
    if metodo_selecionado == 1:
        metodo = detect_integration_method(sympify(expressao), symbols(variavel))
        print(f"\nMétodo de integração selecionado automaticamente: {metodo}")
    elif metodo_selecionado == 2:
        metodo = "Integração por substituição"
    elif metodo_selecionado == 3:
        metodo = "Integração por partes"
    elif metodo_selecionado == 4:
        metodo = "Integração por frações parciais"
    else:
        print("Opção inválida. Usando detecção automática de método.")
        metodo = detect_integration_method(sympify(expressao), symbols(variavel))
        print(f"\nMétodo de integração selecionado automaticamente: {metodo}")

    resultado = calcular_integral(expressao, variavel, metodo, limite_inferior, limite_superior)
    print(f"\nResultado da integração: {resultado}")

if __name__ == "__main__":
    main()