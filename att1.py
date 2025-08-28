nomes = []
while True:
    print("\n1 - Adicionar nome")
    print("2 - procurar nome")
    print("3 - Alterar nome")
    print("4 - Excluir nome")
    print("5 - Listar nomes")
    print("0 - Sair")
    opc = input("Escolha uma opção: ")

    if opc == "1":
        nome = input("Digite um nome para adicionar: ")
        nomes.append(nome)
        print("Nome adicionado com sucesso!")
    elif opc == "2":
        nome = input("Digite o nome que deseja procurar: ")
        if nome in nomes:
            print("Nome encontrado")
        else:
            print("Nome não encontrado")
    elif opc == "3":
        antigo = input("Digite o nome que deseja alterar: ")
        if antigo in nomes:
            novo = input("Digite o novo nome: ")
            pos = nomes.index(antigo)
            nomes[pos] = novo
            print("Nome alterado com sucesso")
        else:
            print("Nome não encontrado")
    elif opc == "4":
        nome = input("Digite o nome que deseja excluir: ")
        if nome in nomes:
            nomes.remove(nome)
            print("Nome removido com sucesso")
        else:
            print("Nome não encontrado")
    elif opc == "5":
        print("Lista de nomes:", nomes)
    elif opc == "0":
        break
    else:
        print("Opção inválida")