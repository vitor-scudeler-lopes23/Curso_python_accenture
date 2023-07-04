import operator

def calculadora():
    operacoes = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    while True:
        expressao = input("Digite um cálculo (ou 'sair' para encerrar): ")

        if expressao.lower() == 'sair':
            print("Encerrando a calculadora...")
            break

        partes = expressao.split()
        if len(partes) != 3:
            print("Formato inválido! O cálculo deve ter o formato: número1 operador número2")
            continue

        numero1, operador, numero2 = partes
        if not (numero1.isdigit() and numero2.isdigit()):
            print("Entrada inválida! Os números devem ser inteiros.")
            continue

        numero1 = int(numero1)
        numero2 = int(numero2)

        if operador not in operacoes:
            print("Operador inválido! Operações suportadas: +, -, *, /")
            continue

        operacao = operacoes[operador]

        try:
            resultado = operacao(numero1, numero2)
            print("Resultado:", resultado)
        except ZeroDivisionError:
            print("Erro! Divisão por zero não é permitida.")
        except Exception as e:
            print("Ocorreu um erro durante o cálculo:", e)

calculadora()