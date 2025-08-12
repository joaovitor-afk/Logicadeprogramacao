#estrutura de decisao
'''nome = input('digite seu nome: ')
idade = input('digite sua idade: ')
if int(idade) >= 18:
    print(f'{nome} é maior de idade')
    print('voce esta dentro do bloco IF')
else:
    print(f'{nome} é menor de idade')
    print('voce esta no bloco ELSE')
    print('voce esta fora da estrutura condicional if else')'''
#LINK - aula if else
'''print(40*'=','BOLETIM ESCOLAR', 40*'=') #upper caixa alta; lower caixa baixa
nome_aluno = input('Digite o nome do aluno: ').upper()
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4)/4

# >=7: aprovado
# >=5: recuperação
# reprovado 

if media >=7:
   print(f'{nome_aluno}!!!Aluno Aprovado!')
   print(f'Nota 1: {nota1} | Nota 2: {nota2}')
   print(f'Nota 3: {nota3} | Nota 4: {nota4}' )
   print(20*'=')
   print(f'Média: {media}')

elif media >=5:
   print(f'{nome_aluno}!!!Aluno de Recuperação!')
   print(f'Nota 1: {nota1} | Nota 2: {nota2}')
   print(f'Nota 3: {nota3} | Nota 4: {nota4}' )
   print(20*'=')
   print(f'Média: {media}')

else:
   print(f'{nome_aluno}!!!Aluno Reprovado!')
   print(f'Nota 1: {nota1} | Nota 2: {nota2}')
   print(f'Nota 3: {nota3} | Nota 4: {nota4}' )
   print(20*'=')
   print(f'Média: {media}')'''
#variaveis
'''nome = 'joao'
idade = 11
altura = 1.25

#verificar se o usuario possui os requisitos minimos 
if idade >= 12 and altura >= 1.2: 
    print(f'A entrada de {nome} esta autorizado. ')
else:
    print(f'A entrada de {nome} nao esta autorizada. ')'''
#variaveis 
nome = 'Alex'
idade = 39


#operador ternario 
print(nome, 'e maior de idade.' if idade >= 18 else ' e menor de idade')