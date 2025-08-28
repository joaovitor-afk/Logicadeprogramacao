import os

while True:
    try:
        #usuario imforma o nome do arquivo
        arquivo = input('digite o nome do arquivo (sem extensao): ').strip().lower()

        #abre o arquivo 
        with open(f'{arquivo}.txt', 'r', encoding='utf-8') as f:
            arquivo_aberto = f.read()


        os.system('cls' if os.name == 'nt' else 'clear')

        #mostrar dados do arquivo
        print(arquivo_aberto)

        while True:
            prosseguir = input('deseja abrir outro arquivo? s/n: ')
            if prosseguir == 's' or prosseguir == 'n':
                break
            else:
                print('opcao invalida')
                continue
        match prosseguir:
            case 's':
                continue
            case 'n':
                break

    except Exception as e:
        print(f'nao foi possivel ler o arquivo. {e}')
        continue



