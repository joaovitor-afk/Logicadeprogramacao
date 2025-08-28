#NOTE - importação da biblioteca random
import random
#NOTE - declaração de variaveis
usuario = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
#NOTE - definir as idades indicativas dos filmes

idade_indicativa_filmes = {
    "Homen Aranha": 12,
    "Batman": 14,
    "Deadpool": 18,
    "Toy Story": 0,
    "Invocação do mal": 17
}

#NOTE - montar a cadeia de repetição para escolha do filme

filmes_lista = ["Homen Aranha", "Batman", "Deadpool", "Toy Story", "Invocação do mal"]

while True:
    print("Escolha um filme:")
    print("1 - Homen Aranha")
    print("2 - Batman")
    print("3 - Deadpool")
    print("4 - Toy Story")
    print("5 - Invocação do mal")
    escolha = int(input("Digite o número do filme que deseja assistir: "))

#NOTE - verificação da idade do usuario para o filme escolhido

#NOTE - entrega de ticket com letra da sala e numero do banco

    if 1 <= escolha <= 5:
        filme = filmes_lista[escolha - 1]
        idade_indicativa = idade_indicativa_filmes[filme]
        if idade >= idade_indicativa:
            ticket = random.randint(0, 999)
            letra_ticket = random.choice(['A', 'B', 'C', 'D'])
            print(f"Seu ticket para assistir {filme} é: {ticket} {letra_ticket}")
            break
        
#NOTE - quebra do loop caso o usuario não tenha idade suficiente para o filme escolhido

        else:
            print(f"Desculpe, você não pode assistir {filme}. Idade mínima: {idade_indicativa}")
            print("Escolha outro filme.")
    else:
        print("Opção inválida.")

        #NOTE - fim do código