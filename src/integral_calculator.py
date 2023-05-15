from sympy import sympify, integrate, symbols, exp
from sympy.integrals.manualintegrate import integral_steps

def detect_integration_method(expression, variable):
    result = integral_steps(expression, variable)
    return result.__class__.__name__

def calcular_integral(expressao, variavel):
    expressao_sym = sympify(expressao)
    variavel_sym = symbols(variavel)
    integral_sym = integrate(expressao_sym, variavel_sym)
    return integral_sym

def main():
    print("Bem-vindo à Calculadora de Integrais!")

    while True:
        expressao = input("\nDigite a expressão a ser integrada: ")
        variavel = input("Digite a variável de integração: ")
        
        metodo = detect_integration_method(sympify(expressao), symbols(variavel))
        print(f"\nMétodo de integração selecionado automaticamente: {metodo}")

        resultado = calcular_integral(expressao, variavel)
        print(f"\nResultado da integração: {resultado}")

        continuar = input("\nDeseja realizar outro cálculo? (s/n): ")
        if continuar.lower() != 's':
            print(f"\nFinalizando a calculadora. Até logo!\n")
            break

if __name__ == "__main__":
    main()