#NOTE -  crie um programa que indique o preço do

while True:
    try:
        #entrada de dados
        etanol = float(input('digite o preço do etanol: ').replace(',','.'))
        gasolina = float(input('digite o preço da gasolina: ').replace(',','.'))
        calculo = (etanol/gasolina)*100
        resultado = "Gasolina" if calculo > 70 else "etanol"

        print(f'Resultado = {calculo:.2f}%. compensa abastecer com {resultado}.')

        opcao = input('Deseja refazer o calculo? (s/n)').lower().strip()
        match opcao:
            case 's':
                continue
            case 'n':
                break
            case _:
                print(f'opcao invalida ')
                continue
    except Exception as e:
        print(f'nao foi possivel executar a operaçao {e}')
        continue  