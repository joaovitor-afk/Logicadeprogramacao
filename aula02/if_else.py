#FIXME - concatenação com + 

nome = "joao"
idade = 16
altura = 1.92

# saida de dados
print('Ola, meu nome e, ' + nome + ', tenho ' + str(idade) + ' anos de idade')

#FIXME - concatenação com , 
print('Ola, meu nome e,', nome,',tenho', idade, 'anos de idade')

#FIXME - concatenação com format
print('Ola, meu nome e, {} , tenho {} anos de idade'.format(nome,idade))

#FIXME - concatenação com f-string 
print(f'Ola, meu nome e, {nome} e tenho {idade} anos de idade')


# eliminando quebra de linha 
print('O Sabio sabia ', end='')
print('que o sabia sabia assobiar')


valor = 1.23456789
# exibindo o valor com duas casas depois da virgula
print(f'{valor:.2f}')

print(50*'=')
peso = input('digite seu peso: ').replace(',','.')
peso = float(peso)
print(peso)
print(f'{peso:.2f}')

