nome_aluno= input ('Qual o nome do aluno?')
nota1= float(input('Qual foi a nota do aluno na primeira prova?'))
nota2= float(input('Qual foi a nota do aluno na segunda prova?'))
nota3= float(input('Qual foi a nota do aluno na terceira prova?'))

soma_notas = nota1 + nota2 + nota3
resultado = soma_notas / 3

print('O aluno ' + nome_aluno + ' ficou com uma média de = ' + str(resultado))