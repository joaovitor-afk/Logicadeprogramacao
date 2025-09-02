import os

valor = 0

lista_cadastro = []

def cadastrar():
    lista_cadastro.append(input('Digite seu nome: '))
    lista_cadastro.append(input('Digite sua idade: '))
    lista_cadastro.append(input('Digite seu cpf: '))
    return 

print(lista_cadastro)
def exibir_dados():

   print(f'seu saldo é: {valor}')
   print(f'nome: {lista_cadastro[0]}')
   print(f'idade: {lista_cadastro[1]}')
   print(f'cpf: {lista_cadastro[2]}')
   return


def deposito():
    global valor
    valor += float(input(f'Digite o quanto voce quer depositar: '))
    return 

def saque():
    global valor
    saque1 = input('digite o valor que deseja sacar: ')
    if valor < saque:
        print('voce nao tem dinheiro suficiente para este saque! ')
    else:
        print('saque feito com êxito')
        valor = valor - saque1
        print(f'o seu saldo é {valor}')
    return
    
    

def encerrar():
    global valor
    del(lista_cadastro)
    print(f'A conta {lista_cadastro}  foi deletada ')
    valor = 0

def menu():
    print('BEM VENDO AO BANCO BANCO')
    p = [['1 - Cadastrar nova conta.'],
        ['2 - Exibir dados da conta.'],
            ['3 - Depositar na conta.'],
            ['4 - Sacar um valor da conta.'],
            ['5 - Encerrar conta'],
            ['6 - Sair do sistema.']]
    for i in p:
        print(i)
    opc = input('Informe a opção desejada: ')

    match opc:
        case '1':
            cadastrar()
        case '2':
            exibir_dados()
        case '3':
            deposito()
        case '4':
            saque()
        case '5':
            encerrar()
        case '6':
            sair()

def sair():

    print('saindo do sistema...')
    exit()

while True:
    menu()

