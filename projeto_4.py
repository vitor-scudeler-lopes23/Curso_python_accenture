def calcular_estatisticas_notas(notas):
    try:
        for nota in notas:
            float(nota)
    except ValueError:
        print("Erro: Insira apenas números como notas.")
        return

    media = sum(notas) / len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)

    print("Média final:", media)
    print("Maior nota:", maior_nota)
    print("Menor nota:", menor_nota)


notas = []
for i in range(4):
    while True:
        try:
            nota = float(input("Digite a {}ª nota: ".format(i+1)))
            break
        except ValueError:
            print("Erro: Insira apenas números como notas.")

    notas.append(nota)

calcular_estatisticas_notas(notas)