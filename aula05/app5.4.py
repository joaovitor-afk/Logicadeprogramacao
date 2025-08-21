import os

while True:
    try:
        novo_texto = input('Digite o texto \n')
        nome_arquivo = input('digite o nome do arquivo (sem extensao): ').strip().lower()

        with open(f'aula05/{nome_arquivo}.txt', 'w', encoding='utf-8') as f:
            f.write(novo_texto)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'{nome_arquivo}.txt gravado com sucesso.')

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
        print(f'nao deu certo coloque os dados corretos')