# ontagem regressiva    

#NOTE - aula 03


#importando biblioteca

'''import os 
from time import sleep

cont = input('Digite um numero inteiro: ')

try:
    cont_int = int(cont)
    while cont_int >= 0:
        os.system('cls')
        print(f'contagem regressiva: {cont_int}...')
        sleep(1)
        cont_int -= 1 
        os.system('cls')
except: 
    print('digite um numero valido')

print("fim da contagem")


programa sorteio 

#NOTE - import biblioteca

import random 

nome1 = input('digite o primeiro nome: ')
nome2 = input('digite o segundo nome: ')
nome3 = input('digite o terceiro nome: ')
nome4 = input('digite o quarto nome: ')
nome5 = input('digite o quinto nome: ')

lista_nomes = [nome1, nome2, nome3, nome4, nome5]

escolhido = random.choice(lista_nomes)
print(escolhido)


#NOTE - import biblioteca lsit sorteio

import random 

lista = []

sair = False


while sair == False: 
    nome_candidato = input('digite os nomes dos candidatos ou enter no vazio para sair: ')
    if nome_candidato != "":
        #append
        lista.append(nome_candidato)
    else:
        sair = True
escolhido = random.choice(lista)

print('escolha foi: ',escolhido)



#sorteio 3

#import lib
import random
import os 
import time

lista_nomes = []
lista_sorteados = []

while True:
    nome = input('Digite o nome para o sorteio: ')
    if nome:
        lista_nomes.append(nome)
    else:
        break

while True:
     if lista_nomes:
            os.system('cls')
            escolhido = random.choice(lista_nomes)
            lista_sorteados.append(escolhido)
            # exclui o sorteado da lista final 
            
            pop - remove pelo indice
                po() - remover o ultimo indice 
                pop(0) - remove o indice 0
            del - intrução, remover item pelo indice, mais de um item
                deldel[3] - busca o indeice 3 e remove ele 
                del[2:10] - vai de 2 á 10 

            remove - remove a partir de uma variavel 
                lista.remove(variavel)

            
            print(f'O escolhido do foi: {escolhido} ')

            lista_nomes.remove(escolhido)



            opcao = input('deseja sortear outro nome? S - sim \n| N - não\n: ').lower()
            os.system('cls')

            if opcao != 's':
                break
     else:
        print('nao a nomes para serem sorteados! ')
        break 
print('Programa finalizado!')
print(f'Os sorteados foram {lista_sorteados}')


#import lib

from random import randint

print("tente adivinhar o numero:!")
num1 = int(input("Digite um numero "))

num_cecret =  randint(1,10)

if num1 == num_cecret:
    print('Parabens, voce ganhou!')
else:
    print('voce perdeu!')
    print(f'o numero escolhido era {num_cecret}') 
    

# v2

import random 

import os

import time

num_secret = random.randint(1,100)

tentativas = 0 

max_tentativas = 10

acertou = False

print(30*'-', 'Bem viado ao adivinha ai zé' ,30*'-')
print(f'voce tem {max_tentativas} tentativas para adivinhar o numero secreto')
print('vamos começar')

while tentativas < max_tentativas:
    try:
        # entrada do usuario
        palpite = int(input('digite o seu palpite: '))

    except ValueError:
        print('Por favor, digite um numero valido ')
        continue 

    tentativas += 1

    #verificar palpite
    if palpite == num_secret:
        acertou = True
        break
    elif palpite < num_secret:
        print('tente um numero maior')
        time.sleep (3)
        os.system('cls')
        
    else:
        print('tente um numero menor')
        time.sleep (3)
        os.system('cls')
        

if acertou:
    print(f'voce acertou o numero {num_secret} em {tentativas} tentativas')
else:
    print(f'errou bobao era {num_secret}')'''