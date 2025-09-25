import json
 
with open("Aula11/bibli.json", "r", encoding="utf-8") as f:
    livro_novo = dict(json.load(f))

class Livros:
    def __init__(self, nome="", autor=""):
        self.__nome = nome
        self.__autor = autor 
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, novo_autor):
        self.__autor = novo_autor

    def salvar(self):
        global livro_novo
        with open("Aula11/bibli.json", "w", encoding="utf-8") as f:
            json.dump(livro_novo, f, ensure_ascii=False, indent=4)

    def adicionar(self):
        global livro_novo
        livro = {
            "nome": input('Digite o nome do livro: ').strip().title(),
            "autor": input('Digite o nome do autor do livro: ').strip().title()
        }
        livro_novo["Livros"].append(livro)
        self.salvar()
        print("Livro adicionado com sucesso")

    def listar(self):
        global livro_novo
        if not livro_novo["Livros"]:
            print("Nenhum livro cadastrado")
        else:
            print("\nLista de livros:")
            for i, livro in enumerate(livro_novo["Livros"], start=1):
                print(f"{i}. Titulo: {livro['nome']} | Autor: {livro['autor']}")
            print("")

    def atualizar(self):
        global livro_novo
        self.listar()
        nome = input("Digite o nome do livro que deseja atualizar: ").strip().title()
        
        for livro in livro_novo["Livros"]:
            if livro["nome"] == nome:
                novo_nome = input("Novo nome (ou deixe em branco para não alterar): ").strip().title()
                novo_autor = input("Novo autor (ou deixe em branco para não alterar): ").strip().title()
                
                if novo_nome:
                    livro["nome"] = novo_nome
                if novo_autor:
                    livro["autor"] = novo_autor

                self.salvar()
                print("Livro atualizado com sucesso")
                return
        
        print("Livro não encontrado")

    def remover(self):
        global livro_novo
        self.listar()
        nome = input("Digite o nome do livro que deseja remover: ").strip().title()
        
        for livro in livro_novo["Livros"]:
            if livro["nome"] == nome:
                livro_novo["Livros"].remove(livro)
                self.salvar()
                print("Livro removido com sucesso")
                return
        
        print("Livro não encontrado")

def menu():
    livro = Livros()
    while True:
        print(20*'=','BEM VINDO A BIBLIOTECA', 20*'=')
        print("1 - Adicionar livro")
        print("2 - Listar livros")
        print("3 - Atualizar livro")
        print("4 - Remover livro")
        print("5 - Sair")
        print(64*'=')

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            livro.adicionar()
        elif opcao == "2":
            livro.listar()
        elif opcao == "3":
            livro.atualizar()
        elif opcao == "4":
            livro.remover()
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida")

menu()