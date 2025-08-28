#exercício 2
numeros = []
while True:

    valor = input('digite um numero ou escolha sair: ')
    if valor.lower() == 'sair':
        break 
    numeros.append(int(valor))

    numeros.sort()
    print(f'numeros em ordem crescente: .{numeros}')