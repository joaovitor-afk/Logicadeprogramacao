#NOTE -  coleção listas, dicionario, tuplas, 

#NOTE -  lista []

''' nomes_lista = ['joao', 'maria', 'carlos']

#NOTE -  range  |  len conta lista

for i in range(len(nomes_lista)):
    print(f'{i + 1}º nome: {nomes_lista[i]}')

#NOTE -  for para listar 

#NOTE - sort ordenar

nomes_lista.sort()

#NOTE - if in para encontrar valor

nome = input('Informe o nome que deseja encontrar: ')

if nome in nomes_lista:
    print(nome)
else: 
    print(f'{nome} nao encontrado. ')

    #NOTE - index

    indice = nomes_lista.index(nome)

    #retornar resultado
    try:
        print(f'{nome} encontrado no indice {indice}. ')
    except:
        print(f'{nome} nao encontrado. ')

#NOTE - count 

quantidade = nomes_lista.count(nome)

try:
    print(f'{nome} foi encontrado na listas {quantidade} vezes. ')
except:
    print(f'{nome} nao encontrado ') '''

#NOTE -  alterando dados da lista 

'''print(nomes_lista)

nomes_lista[0] = 'alex' 

for nome in nomes_lista:
    print(nome)

#NOTE - usuario alterar input

nomes_lista = ['joao', 'maria', 'carlos']

nome_a_alterar = input('informe o nome que deseja alter: ')

nomes_lista[nomes_lista.index(nome_a_alterar)] = input('informe o novo nome: ')

print(nomes_lista)

#NOTE - tabuada

numero = int(input('Digite seu numero: '))

for i in range(1, 11):
    resultado = numero * i
    print(f'{i} X {numero} = {resultado}')'''


