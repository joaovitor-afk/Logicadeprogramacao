# revisao
'''
nome = "sybal"
idade = 16

print(type(nome)) # ver o tipo de dados da variavel

idade = float(idade)

print(f'o meu nome é {nome} {type(nome)} tenho {idade} anos de idade {idade} ')

nome_usuario = input("digite seu nome: ") # padrao string

peso = float(input("digite seu peso").replace(',','.').lower())

if peso >=50: # verificar se e verdade
    print('acima de 50 kilos')
else # se nao for verdadeiro


problema: crie um sistema de indice corporal(IMC) do usuario
mostre na telaseu peso e se deve emagrecer ou nao 
imc = peso/(altura * altura)

Classificação do IMC

Faixa de IMC (kg/m²)

Abaixo do peso
Menos de 18,5

Peso normal
18,5 a 24,9

Sobrepeso
25 a 29,9

Obesidade grau I
30 a 34,9

Obesidade grau II
35 a 39,9

Obesidade grau III
40 ou mais
'''

'''print(40*"-",'CALCULADORA DE IMC',40*'-')
altura = float(input('digite sua altura:' ).replace(',','.'))
peso = float(input('digite seu peso:' ).replace(',','.'))

imc = peso / (altura * altura)
print()
print(f'seu IMC é: {imc:.2f}')

if imc <= 18.5:
    print('abaixo do normal')
elif imc <= 24.9:
    print('normal')
elif imc <= 29.9:
    print('sobrepeso')
elif imc <= 24.9:
    print('sobrepeso grau I')
elif imc <= 34.9:
    print('obesidade')
elif imc <= 24.9:
    print('obesidade grau 1')
elif imc <= 39.9:
    print('obesidade grau II')
elif imc >40:
    print('obesidade grau III')'''
    
'''
problema 2: um elevador de caraga possui capacidade para 200kg. crie um programa que receba
 so usuario seu peso e o peso da carga e verifica se a carga está autoriazada a usar o elvador ou nao.
 '''

'''print(40*"-",'VERIFICACAO DE ENTRADA',40*'-')
peso = float(input('digite seu peso:' ).replace(',','.'))

carga = float(input('digite o peso da sua carga:' ).replace(',','.'))

carga_final = peso + carga

if carga_final < 200:
    print('voce esta autorizado a entrar')
else:
    print ('seu peso total nao esta autoriazado a entrar, retire a carga para entrar')
    #NOTE -  codigo de verificaçao de peso e carga para elevador
    '''
    #NOTE - laços de repetiçao

'''numero = 10 

#loop
while numero >= 0:
    print(numero)
    numero += 1'''

'''#continue

cont = 0

while cont < 10:
    cont += 1
    if cont % 2 == 0:
        print(cont)
    else:
        continue

    print('contando...')'''

'''#break use

cont = 0 
while cont < 15:
    cont += 1
    if cont % 2 == 0:
        print(cont)
    elif cont >= 7:
        break
    else:
        continue

    print('contando...')'''

'''#NOTE -  teste while break

while True:
    print(40*"-",'CALCULADORA DE IMC',40*'-')
    altura = float(input('digite sua altura:' ).replace(',','.'))
    peso = float(input('digite seu peso:' ).replace(',','.'))

    imc = peso / (altura * altura)
    print()
    print(f'seu IMC é: {imc:.2f}')

    if imc <= 18.5:
        print('abaixo do normal')
    elif imc <= 24.9:
        print('normal')
    elif imc <= 29.9:
        print('sobrepeso')
    elif imc <= 24.9:
        print('sobrepeso grau I')
    elif imc <= 34.9:
        print('obesidade')
    elif imc <= 24.9:
        print('obesidade grau 1')
    elif imc <= 39.9:
        print('obesidade grau II')
    else: 
        print('obesidade grau III')

    opcao = input('deseja calcular novamente? S - Sim | N Nao').lower()
    
    if opcao == 's':
        continue
    elif opcao == 'n':
        print('saindo do sistema!')
        break
    else:
        print('opcao invalida')
        break'''
'''print(40*"-",'Cadastro',40*'-')
nome = input('digite seu nome: ')
cpf = input('digite seu cpf: ')
telefone = input('digite seu numero: ')
dt_nascimento = input("digite seu ano de nascimento: ")
print(80*"=")
while True:
    print(40*"-",'Sistema Concole 2DS',40*'-')
    print()
    print('1 - Clculadora IMC')
    print('2 - Maior Idade ')
    print('3 - Calculadora')
    print('4 - Dados Pessoais')
    print('5 - Feliz Natal')
    print('6 - Sair')

    opcao = input('digite uma opcao: ')

    if opcao == "1":
        print(40*"-",'CALCULADORA DE IMC',40*'-')
        altura = float(input('digite sua altura:' ).replace(',','.'))
        peso = float(input('digite seu peso:' ).replace(',','.'))
        imc = peso / (altura * altura)
        print()
        print(f'seu IMC é: {imc:.2f}')
        if imc <= 18.5:
            print('abaixo do normal')
        elif imc <= 24.9:
            print('normal')
        elif imc <= 29.9:
            print('sobrepeso')
        elif imc <= 24.9:
            print('sobrepeso grau I')
        elif imc <= 34.9:
            print('obesidade')
        elif imc <= 24.9:
            print('obesidade grau 1')
        elif imc <= 39.9:
            print('obesidade grau II')
        else: 
            print('obesidade grau III')

    elif opcao == "2":
        ano_atual = 2025
        idade = ano_atual - dt_nascimento
        print(nome, 'e maior de idade.' if idade >= 18 else ' e menor de idade')

    elif opcao == "3":
         print('calculadora')
        
         while True:
            num1 = float(input("digite o primeiro numero: "))
            num2 = float(input('digite o segundo numero: '))
            print('1 - soma')
            print('2 - divisao')
            print('3 - subtraçao')
            print('4 - multiplicaçao')
            print('5 - sair')

            opcao_calculo = input('escolha uma operaçao matematica: ')

            

            if opcao_calculo == "1":
                print(f"resultado da soma é: {num1 + num2} ")
            elif opcao_calculo == '2':
                print(f"resultado da divisao é: {num1 / num2} ")
            elif opcao_calculo == '3':
                print(f"resultado da subtraçao é: {num1 - num2} ")
            elif opcao_calculo == '4':
                print(f"resultado da multiplicaçao é: {num1 * num2} ")
            elif opcao_calculo == '5':
                break
            else: 
                print('opçao invalida')
    elif opcao == "4":
        print(35*'_')
        print(f'| Nome: {nome} | Telefone: {telefone} |')
        print(f"| CPF: {cpf} | Dta de Nascimento: {dt_nascimento} | ")
        print(35*'_')
    elif opcao == "5":
        linhas = 20
        i = 1

        while i<= linhas:
            espacos = linhas - i 
            estrelas = 2 * i - 1

            print(" " * espacos + "*" * estrelas)
            i +=1
    elif opcao == "6":
        print("saindo do sistema!")
        break
    else:
        print("Opcao invalida!")'''
#NOTE - fim do programa 

nome = 'sybal'

for i in nome: 
    print(i)